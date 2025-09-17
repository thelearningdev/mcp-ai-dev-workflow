---
layout: blue-title-slide
---

# MCP Best Practices

---
layout: blue-sidebar
---

::header::

## MCP - What not to do?

There are 5 metrics to evaluate the effectiveness of a prompt:

::content::

<v-clicks>

- MCP as a wrapper for REST APIs
- Consumers are Agents not humans
- Less is more
- Using all the primitives

</v-clicks>

---
layout: blue-sidebar
---

::header::

## MCP - Problems and Tradeoffs

There are three ways to measure effectiveness

::content::

<v-clicks>

- Scaling
  - How are stateful systems going to scale and preserve the context?
- Auth & Permissions
  - How to handle permissions of users
- Tool Discovery
  - How to expose tools based on permission that a specific user have?

</v-clicks>

---
layout: blue-sidebar
---

::header::

## MCP Server Security Issues


::content::

<v-clicks>

- Prompt Injection
- Code-in-the-middle-attack
- MCP stealing data from local machine

</v-clicks>

---
layout: blue-sidebar
---

::header::

## Relevance

Does the output stay on-topic?

::content::

<v-click>

**Example:**
  - Prompt: `Explain photosynthesis.`
  - ❌ Output: "In cooking, photosynthesis isn't important."
  - ✅ Output: "Photosynthesis is the process by which plants convert sunlight into energy..."

</v-click>
<v-click>

**How to measure?**

```
def relevance_score(response, expected_content):
    return semantic_similarity(response, expected_content)
```

</v-click>

---
layout: blue-sidebar
---

::header::

## Consistency

Does it give reliable results repeatedly?

::content::

<v-clicks>

**How to measure?**

  - Run same prompt 3–5 times
  - Compare factual correctness & tone

```
def consistency_score(responses: list):
    similarities = []
    for i in range(len(responses)):
        for j in range(i+1, len(responses)):
            similarity = semantic_similarity(responses[i], responses[j])
            similarities.append(similarity)
    return np.mean(similarities)
```
</v-clicks>

---
layout: blue-sidebar
---

::header::

## Accuracy

Is the information factually correct?

::content::

<v-click>

- **Example:**
  - Prompt: `What is the capital of Canada?`
  - ❌ "Toronto"
  - ✅ "Ottawa"

**How to measure?**

```
def accuracy_score(response: str, ground_truth):
    return semantic_similarity(response, ground_truth)
```
</v-click>

---
layout: blue-sidebar
---

::header::

## Efficiency

Uses minimal tokens for max value

::content::

<v-click>

**Example:**
  - ❌ "The process of cell division, known as mitosis, is when cells divide."
  - ✅ "Mitosis is cell division."

**How to measure**

  ```
  def prompt_efficiency_score(responses, ground_truth, weights=None):
    weights = weights or {"accuracy": 0.4, "consistency": 0.4, "brevity": 0.2}

    consistency = consistency_score(responses)
    accuracy = accuracy_score(responses, ground_truth)
    brevity = np.mean([1 / (len(r.split()) + 1) for r in responses])
    
    return weights["accuracy"] * accuracy + weights["consistency"] * consistency + weights["brevity"] * brevity
  ```

</v-click>

---
layout: blue-sidebar
---

::header::

## User Satisfaction

::content::

- Ask user to rate ⭐️
  - Was this helpful?
- Use Likert scale or thumbs up/down
- Capture subjective value