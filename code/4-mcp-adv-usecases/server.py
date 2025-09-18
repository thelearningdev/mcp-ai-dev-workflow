from data import lms_data
import asyncio

from fastmcp import FastMCP
from middleware import RoleAuthMiddleware
import json
from mcp.server.auth.provider import AccessToken, TokenVerifier
from utils import get_user


mcp = FastMCP("lms-mcp")
mcp.add_middleware(RoleAuthMiddleware())


def compute_level(score: int):
    rules = lms_data["recommendation_rules"]
    if score == 5:
        return rules["5"]
    elif score == 3:
        return rules["3"]
    elif score == 2:
        return rules["2"]
    else:
        return rules["other"]


# --- Tools ---
@mcp.tool(tags="student")
def take_assessment(student_id: str, subject: str, answers: dict) -> str:
    """Students take an assessment for a subject. Returns their level and recommended courses."""
    student = get_user(student_id)
    if not student or student["role"] != "student":
        return json.dumps({"error": "Not a student"})

    score = sum(1 for _, correct in answers.items() if correct)
    student["exam_scores"][subject] = score
    level = compute_level(score)

    courses = []
    for trainer in lms_data["users"]["trainers"]:
        if trainer["category"].lower() == subject.lower():
            courses = [c for c in trainer["courses"] if c["level"] == level]

    return json.dumps(
        {
            "student": student["name"],
            "subject": subject,
            "score": score,
            "level": level,
            "recommended_courses": courses,
        }
    )


@mcp.tool(tags=["student"])
def get_recommendations(student_id: str) -> str:
    """Fetch course recommendations for a student across all subjects."""
    student = get_user(student_id)
    if not student or student["role"] != "student":
        return json.dumps({"error": "Not a student"})

    recs = {}
    for subject, score in student["exam_scores"].items():
        level = compute_level(score)
        for trainer in lms_data["users"]["trainers"]:
            if trainer["category"].lower() == subject.lower():
                recs[subject] = [c for c in trainer["courses"] if c["level"] == level]

    return json.dumps({"student": student["name"], "recommendations": recs})


@mcp.tool(tags=["trainer"])
def add_course(sme_id: str, course: dict) -> str:
    """trainer adds a new course to their category."""
    trainer = get_user(sme_id)
    if not trainer or trainer["role"] != "trainer":
        return json.dumps({"error": "Not an trainer"})

    trainer["courses"].append(course)
    return json.dumps({"message": "Course added", "courses": trainer["courses"]})


@mcp.tool(tags=["trainer"])
def remove_course(sme_id: str, course_id: str) -> str:
    """trainer removes a course from their category."""
    trainer = get_user(sme_id)
    if not trainer or trainer["role"] != "trainer":
        return json.dumps({"error": "Not an trainer"})

    trainer["courses"] = [c for c in trainer["courses"] if c["id"] != course_id]
    return json.dumps({"message": "Course removed", "courses": trainer["courses"]})


@mcp.tool(tags=("trainer", "student"))
def list_courses_of_expert(sme_id: str) -> str:
    """List courses for an trainer."""
    trainer = get_user(sme_id)
    if not trainer or trainer["role"] != "trainer":
        return json.dumps({"error": "Not an trainer"})
    return json.dumps({"trainer": trainer["name"], "courses": trainer["courses"]})


# --- Entry Point ---
if __name__ == "__main__":
    mcp.run(transport='streamable-http', uvicorn_config={"reload":True, 'log_level': 'debug'})
