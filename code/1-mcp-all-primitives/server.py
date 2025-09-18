from mcp.server.fastmcp import FastMCP, Context
from pydantic import BaseModel

mcp = FastMCP(name="1-MCP-all-primitives")


class User(BaseModel):
    name: str
    age: int | None = None


@mcp.tool()
async def register_user(user: User, ctx: Context):
    if not user.age:
        await ctx.debug("creating user without age")
    return f"hello {user.name}"


@mcp.resource("weather://{city}/current")
def get_weather(city: str) -> dict:
    """Provides weather information for a specific city."""
    return {
        "city": city.capitalize(),
        "temperature": 22,
        "condition": "Sunny",
        "unit": "celsius",
    }


@mcp.resource(
    "file:///Users/bhavaniravi/projects/courses/mcp-course/code/1-mcp-all-primitives/server.py"
)
def get_file() -> dict:
    """Provides weather information for a specific city."""
    return "Content of the file"


@mcp.prompt()
async def get_study_plan(topic: str):
    return f"Generate a study plan for::{topic}"


if __name__ == "__main__":
    print("starting server")
    mcp.run(transport="stdio")
