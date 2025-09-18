# server.py

from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt
import json
from cryptography.fernet import Fernet
import logging

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# In-memory DBs (for demo purposes)
user_db = {"user1": {"password": "pass1", "locations": ["New York", "Paris"]}}
context_store = {}
SECRET_KEY = "supersecretjwtkey"
FERNET_KEY = Fernet.generate_key()
fernet = Fernet(FERNET_KEY)

# Logging
logging.basicConfig(level=logging.INFO)

# CORS (if frontend is used)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# === Models ===
class LoginRequest(BaseModel):
    username: str
    password: str


class WeatherQuery(BaseModel):
    location: str
    input: str  # Simulated user input for model


class WeatherResponse(BaseModel):
    response: str


# === Auth ===
def create_token(username: str):
    payload = {"sub": username, "exp": datetime.utcnow() + timedelta(minutes=30)}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")
        if username not in user_db:
            raise HTTPException(status_code=401, detail="Invalid user")
        return username
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


# === Secure Context Handling ===
def load_context(username: str):
    encrypted = context_store.get(username)
    if encrypted:
        return json.loads(fernet.decrypt(encrypted).decode())
    return {}


def save_context(username: str, context: dict):
    encrypted = fernet.encrypt(json.dumps(context).encode())
    context_store[username] = encrypted


# === Simulated MCP + Tool ===
def run_weather_tool(location: str):
    # In real use, integrate with actual weather API here
    if location not in ["New York", "Paris", "London"]:
        raise ValueError("Invalid location.")
    return f"The weather in {location} this weekend is sunny and 22°C."


def run_model(user_input: str, context: dict):
    # Simulated model with memory/context usage
    last_location = context.get("last_location", "unknown")
    return f"Based on your previous interest in {last_location}, I suggest checking {user_input}."


# === Routes ===
@app.post("/login")
def login(request: LoginRequest):
    user = user_db.get(request.username)
    if not user or user["password"] != request.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": create_token(request.username), "token_type": "bearer"}


@app.post("/weather", response_model=WeatherResponse)
def get_weather(query: WeatherQuery, username: str = Depends(verify_token)):
    context = load_context(username)

    # Security: Sanitize input
    location = query.location.strip()
    if not location.isalpha():
        raise HTTPException(status_code=400, detail="Invalid location format")

    # Rate limiting placeholder (add Redis or real limiter in prod)
    logging.info(f"{username} is querying weather for {location}")

    # Run weather tool
    try:
        weather = run_weather_tool(location)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Run simulated model with context
    model_response = run_model(query.input, context)

    # Update context
    context["last_location"] = location
    save_context(username, context)

    return {"response": f"{weather}\n{model_response}"}


# === Audit Logging Middleware ===
@app.middleware("http")
async def audit_logging(request: Request, call_next):
    user = request.headers.get("Authorization", "unknown").replace("Bearer ", "")
    timestamp = datetime.utcnow().isoformat()
    logging.info(
        f"[AUDIT] Time: {timestamp}, User Token: {user}, Path: {request.url.path}"
    )
    return await call_next(request)
