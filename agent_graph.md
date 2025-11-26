# 🧠 Agent Graph – Kasparro Agentic Facebook Performance Analyst

## 🔍 High-level System Flow

User Query (e.g., "Analyze ROAS drop")
↓
Planner Agent
↓
Data Agent
↓
Insight Agent
↓
Evaluator Agent
↓
Creative Agent
↓
Orchestrator
↓
Outputs → insights.json, creatives.json, report.md


---

## 🧠 Agent Responsibilities & Data Flow

| Agent | Role | Input | Output |
|-------|------|-------|--------|
| Planner Agent | Breaks user request into executable steps | User query string | Plan (list of subtasks) |
| Data Agent | Loads CSV & computes metrics | Plan + dataset | DataFrame + summary dict |
| Insight Agent | Generates hypotheses for performance changes | Summary dict | Hypotheses list |
| Evaluator Agent | Validates hypotheses with numeric evidence | Hypotheses + summary | Validated hypotheses (evidence + confidence) |
| Creative Agent | Suggests creative directions for low CTR | Summary + dataset | Creative ideas (headlines + CTAs) |
| Orchestrator | Connects all agents & saves reports | All agent outputs | insights.json, creatives.json, report.md |

---

## 📌 Execution Notes
- 🚀 The **Planner Agent** triggers the workflow based on the user query
- 📊 The **Data Agent** acts as the foundation — all insights depend on its summary metrics
- 🧠 **Insight + Evaluator** form a reasoning loop (hypothesis → validation)
- 🎨 **Creative Agent** is optional but adds marketing strategy value
- 🪄 **Orchestrator** is the controller that runs everything end-to-end

---

This diagram is intentionally simple — it matches the assignment instructions and makes it easy for reviewers to evaluate reasoning structure.