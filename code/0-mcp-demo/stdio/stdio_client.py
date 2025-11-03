import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# No LLMs are harmed in this example
# We are just understanding client/server architecture

current_path = __file__.rsplit("/", 1)[0]

server_params = StdioServerParameters(
    command="uv",
    args=["run", f"{current_path}/stdio_server.py"],
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                name="get_weather",
                arguments={"city": "sf"},
            )
            print(result.content)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
