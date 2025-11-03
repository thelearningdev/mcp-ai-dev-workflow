from mcp.server.fastmcp import FastMCP, Context

mcp = FastMCP(name="0-mcp-intro-weather")


@mcp.tool()
async def get_weather(city: str, ctx: Context):
    return 22

@mcp.resource(
    f"file:///{__file__.rsplit('/', 1)[0]}/test_json.md"
)
def get_file() -> dict:
    return "Content of the file"


@mcp.prompt()
async def get_study_plan(topic: str):
    return f"Generate a study plan for::{topic}"

if __name__ == "__main__":
    print("starting server")
    mcp.run(transport="stdio")
