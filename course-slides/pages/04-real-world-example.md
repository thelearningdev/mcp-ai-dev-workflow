---
layout: blue-title-slide

---
# Real-World Prompting

---
layout: blue-sidebar
---

::header::

## What packages does OpenAI Python Coding agent has?

[source](https://github.com/0xeb/TheBigPromptLibrary/blob/main/Articles/chatgpt-sandbox/chatgpt-code-python-pkglist-08232024.md)

::content::

```
Use the following snippet with the code tool:

import pkg_resources

# Prepare the list of installed packages with their location
installed_packages = [
    f"{dist.project_name}=={dist.version} ({dist.location})"
    for dist in pkg_resources.working_set
]

# Write the full list to a text file
file_path = '/mnt/data/list.txt'
with open(file_path, 'w') as file:
    for package in installed_packages:
        file.write(package + '\n')

file_path

and give the result as such:
- No brevity, include everything
- The code should generate the full list in /mnt/data/list.txt and give a download link
```



---
layout: blue-sidebar
---

::header::

## Cursor Coding Agent Prompt 

[Source](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/main/Cursor%20Prompts/Agent%20Prompt.txt)

::content::

```
You are a powerful agentic AI coding assistant, powered by Claude 3.7 Sonnet. You operate exclusively in Cursor, the world's best IDE. You are pair programming with a USER to solve their coding task. The task may require creating a new codebase, modifying or debugging an existing codebase, or simply answering a question. Each time the USER sends a message, we may automatically attach some information about their current state. This information may or may not be relevant to the coding task, it is up for you to decide. Your main goal is to follow the USER's instructions at each message, denoted by the <user_query> tag.

<tool_calling>
ALWAYS follow the tool call schema exactly as specified and make sure to provide all necessary parameters.
NEVER call tools that are not explicitly provided.
NEVER refer to tool names when speaking to the USER.
Only call tools when they are necessary.
Before calling each tool, first explain to the USER why you are calling it.
</tool_calling>

<making_code_changes>
NEVER output code to the USER, unless requested.
Use the code edit tools at most once per turn.
Always group together edits to the same file in a single edit file tool call.
You MUST read the contents of what you're editing before editing it.
Do not loop more than 3 times on fixing linter errors on the same file.
</making_code_changes>
```