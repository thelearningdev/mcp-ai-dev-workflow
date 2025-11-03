import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

# No LLMs are harmed in this example
# We are just understanding client/server architecture


async def run():
    async with streamablehttp_client(
        url="http://127.0.0.1:8000/mcp",
    ) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print (await session.list_tools())
            result = await session.call_tool(
                name="get_weather",
                arguments={"city": "sf"},
            )
            print(result.content)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
