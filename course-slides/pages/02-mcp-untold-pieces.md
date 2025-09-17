---
layout: blue-title-slide
---

# MCP Primitives

---
title: MCP Primitives
hideInToc: true
layout: blue-sidebar
---

::header::

## MCP Primitives

::content::

<v-clicks>

- **Server**
  - Tools
  - Resources
  - Prompts
- **Client**
  - Sampling
  - Roots
  - Elicitation
- **Notifications**

</v-clicks>

---
title: MCP Server Primitives
hideInToc: true
layout: blue-sidebar
---

::header::

# MCP Server Primitives

::content::

| Feature   | Examples                                | Who controls it |
|-----------|-----------------------------------------|-----------------|
| Tools     | Search flights<br>Send messages<br>Create calendar events | Model |
| Resources | Retrieve documents<br>Access knowledge bases<br>Read calendars | Application |
| Prompts   | Plan a vacation<br>Summarize my meetings<br>Draft an email | User |


---
layout: blue-sidebar
---

::header::

## MCP Client Primitives

::content::

| Feature     | Example          |
|-------------|------------------|
| Sampling    | Handing off LLM Calling responsibility to client |
| Roots       | Read specific files |
| Elicitation | Ask user details  |


---
layout: blue-sidebar
---

::header::

## Sampling

::content::

- Server makes the request back to client to use the LLM
- Server doesn't have to make decisions for client's preferences
- Eg., Research MCP server, some users might like short answers, some like detailed reports with references

![](../assets/sampling-1.png)


---
layout: blue-sidebar
---

::header::

## Notifications

::content::

- Server progress tracking
- Alerting on intermediate steps

![](../assets/notifications.png)


---
layout: blue-sidebar
---

::header::

## Roots

::content::

- Grant permission to specific files
- Client specifying a root has no meaning unless there is a server implementation to support it

![](../assets/roots.png)