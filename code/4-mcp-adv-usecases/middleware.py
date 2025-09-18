from fastmcp.server.middleware import MiddlewareContext, Middleware
from fastmcp.exceptions import ToolError
from data import lms_data
from fastmcp.server.dependencies import get_http_headers



def get_user(user_id: str):
    for trainer in lms_data["users"]["trainers"]:
        if trainer["id"] == user_id:
            return trainer
    for stu in lms_data["users"]["students"]:
        if stu["id"] == user_id:
            return stu
    return None


ROLE_TOOL_MAP = {
    "student": {"take_assessment", "get_recommendations"},
    "trainer": {"add_course", "remove_course", "list_courses"},
}


class RoleAuthMiddleware(Middleware):
    async def on_tool_call(self, context: MiddlewareContext, call_next):
        """
        Intercept tool calls before they hit the actual tool handler.
        Enforce role-based access.
        """
        tool = context.message.name
        args = context.message.arguments
        user_id = args.get("user_id") or args.get("student_id") or args.get("sme_id")

        if not user_id:
            raise ToolError("Access denied: private tool, login first")

        user = get_user(user_id)
        if not user:
            raise ToolError("Access denied: private tool, invalid user id")

        allowed = ROLE_TOOL_MAP.get(user["role"], set())
        if tool not in allowed:
            raise ToolError(f"❌ User {user['name']} ({user['role']}) not authorized to call {tool}")
        return await call_next(context)

    async def on_list_tools(self, context: MiddlewareContext, call_next):
        headers = get_http_headers()
        user_id = headers.get("token", "")
        user = get_user(user_id)

        if not user:
            role = "unauthorized"
        else:
            role = user["role"]

        result = await call_next(context)

        # filter tools that are meant for unauthorized or
        # filter tools based on permissions
        filtered_tools = [tool for tool in result if role not in tool.tags]

        return filtered_tools
