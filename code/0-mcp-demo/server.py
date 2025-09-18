from mcp.server.fastmcp import FastMCP, Context
from mcp.types import SamplingMessage, TextContent

mcp = FastMCP(name="0-mcp-intro-weather")


@mcp.tool()
async def get_weather(city: str, ctx: Context):
    return 22


if __name__ == "__main__":
    print ("starting server")
    mcp.run(transport="stdio")
