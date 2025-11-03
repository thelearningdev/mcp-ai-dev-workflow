
import os
import asyncio
from mcp.server.fastmcp import FastMCP, Context
from mcp.types import SamplingMessage, TextContent


mcp = FastMCP(name="0-mcp-intro-weather")


@mcp.tool()
async def get_weather(city: str, ctx: Context):
    return 22

@mcp.resource(
    f"file:///{__file__.rsplit('/', 1)[0]}/test_json.md"
)
def get_file() -> dict:
    return "Content of the file"


@mcp.tool()
async def summarize(text_to_summarize: str, ctx: Context):
    prompt = f"""
        Please summarize the following text:
        {text_to_summarize}
    """

    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(role="user", content=TextContent(type="text", text=prompt))
        ],
        max_tokens=4000,
        system_prompt="You are a helpful research assistant.",
    )

    if result.content.type == "text":
        return result.content.text
    else:
        raise ValueError("Sampling failed")
    
    
@mcp.tool()
async def add(a: int, b: int, ctx: Context) -> int:
    await ctx.info("Preparing to add...")
    await ctx.report_progress(20, 100)

    await asyncio.sleep(10)

    await ctx.info("OK, adding...")
    await ctx.report_progress(80, 100)

    return a + b

@mcp.tool()
async def list_folders_under_roots(ctx: Context):
    """
    Lists all folders under the client roots (as specified by the MCP client).
    """
    roots = await ctx.session.list_roots()
    if not roots:
        return {"error": "No client roots available in context."}
    
    return {"roots": roots}

if __name__ == "__main__":
    print("starting server")
    mcp.run(transport="stdio")
