# 🚀 Kasparro – Agentic Facebook Performance Analyst  
### Assignment Submission – Applied AI Engineer (Suryansh Tyagi)

---

## 📌 Objective
This project implements a **multi-agent autonomous system** capable of:
- Diagnosing why **ROAS (Return on Ad Spend)** changed over time
- Identifying drivers behind performance fluctuations (CTR, campaign variance)
- Generating **new creative ideas** for low-CTR campaigns using dataset messaging patterns

This system prioritizes **LLM-first reasoning, modularity, and traceability**.

---

## 🧠 Agent Architecture Overview

| Agent | Responsibility |
|-------|---------------|
| Planner Agent | Converts user query into subtasks |
| Data Agent | Loads dataset & computes metrics (ROAS, CTR trends) |
| Insight Agent | Generates hypotheses about performance change |
| Evaluator Agent | Validates hypotheses with quantitative evidence |
| Creative Agent | Suggests new creatives (headlines + CTA) for low-CTR ads |
| Orchestrator | Coordinates all agents and writes outputs |

📌 Detailed flow → see `agent_graph.md`

---

## 📦 Tech Stack & Dependencies

| Component | Library |
|----------|---------|
| Data Processing | pandas |
| Agent Architecture | Python modules |
| Logging | JSON structured logging |
| Configuration | YAML |

---

## 🛠 Setup Instructions

### 1️⃣ Create & activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
