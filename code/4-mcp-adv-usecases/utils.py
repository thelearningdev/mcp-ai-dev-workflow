from data import lms_data

from fastmcp import FastMCP
from middleware import RoleAuthMiddleware

mcp = FastMCP("lms-mcp")
mcp.add_middleware(RoleAuthMiddleware())


def get_user(user_id: str):
    for trainer in lms_data["users"]["trainers"]:
        if trainer["id"] == user_id:
            return trainer
    for stu in lms_data["users"]["students"]:
        if stu["id"] == user_id:
            return stu
    return None
