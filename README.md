# MCP Servers and AI Dev Workflows

A workshop on how MCP servers help you accelerate your development workflows


## Part 1: Intro to MCP

### 1. Setting up Python Environment

Ensure you have python 3.12+ installed

```
cd code
uv sync
uv venv
source .venv/bin/activate
```

### 2. Play with your server

With your virtual env activated run...

```
cd 0-mcp-demo/stdio/
python stdio_server.py
```
The terminal will say `starting server` 

Now paste your JSON-RPC requests line by line, ignore lines starts with #

1. Initialize the client

```
{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test-client","version":"1.0.0"}}}
```

2. initialize the notification

```
{"jsonrpc":"2.0","method":"notifications/initialized"}
```

> Note: You won't receive a JSON response here

3. list the tools

```
{"jsonrpc":"2.0","id":2,"method":"tools/list"}
```

4. call the tool get weather

```
{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"get_weather","arguments":{"city":"London"}}}
```

### 3. Let's visualize these features in MCP inspector

**1. Install `mcp-inspector`**

```
npx @modelcontextprotocol/inspector
```

If you do not have node installed, use brew installation

```
brew install mcp-inspector
mcp-inspector
```

On the MCP inspector that opens on your browser `http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=<some-token-here>` add  


**2. Note down two things**

- Your python environment  
    - Type `which python`you will get an answer like this `<YOUR_BASE_PATH>/mcp-for-ai-dev-course/code/.venv/bin/python` 
- Path to the `stdio_server.py`
    - On vscode, Right click on the `stdio_server.py` file and copy path `<YOUR_BASE_PATH>/mcp-for-ai-dev-course/code/0-mcp-demo/stdio/stdio_client.py` 

> Replace `YOUR_BASE_PATH` with right path according to your laptop

**3. Add these to MCP inspector**

1. Under command - add python path
2. Under Arguments - add stdio_server path

> Note: You can also run

```
npx @modelcontextprotocol/inspector \
  <YOUR_BASE_PATH>/mcp-for-ai-dev-course/code/.venv/bin/python \
  <YOUR_BASE_PATH>/mcp-for-ai-dev-course/code/0-mcp-demo/stdio/stdio_server.py
```


## Part 2: MCP on AI Dev workflow

1. Create an account in [context7](https://context7.com/) and copy your API Key, keep it aside

> We are not affiliated with context7, just a tool that works well

2. You need Vscode + github copilot (free version should do) for this demo

3. Two ways to install MCP server `mcp.json` or MCP extensions

### Demo workflow

1. Create an airflow pipeline without mcp servers
2. Highlight the disadvantages
3. Enable MCP servers
4. Add better instructions

