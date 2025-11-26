# 🚀 Kasparro – Agentic Facebook Performance Analyst
Assignment Submission — Applied AI Engineer (Suryansh Tyagi)

---

## 📌 Objective
This project implements a **multi-agent autonomous AI system** capable of:
- Diagnosing why **ROAS (Return on Ad Spend)** changed over time
- Identifying **root drivers behind performance fluctuation** (CTR drops, campaign fatigue, audience changes)
- Generating **new creative ideas** for low-CTR ad campaigns using dataset messaging patterns

The system focuses on:
✔ LLM-first reasoning  
✔ Modular design  
✔ Observability & traceability  
✔ Production-style pipeline

---

## 🧠 Agent Architecture Overview

| Agent | Responsibility |
|-------|---------------|
| **Planner Agent** | Breaks user query into subtasks |
| **Data Agent** | Loads dataset & computes metrics (Avg ROAS, CTR, variance, trends) |
| **Insight Agent** | Generates hypotheses explaining performance change |
| **Evaluator Agent** | Validates hypotheses using numerical evidence |
| **Creative Agent** | Suggests new creative directions (headlines + CTA) |
| **Orchestrator** | Coordinates the full agent reasoning chain & exports reports |

📌 Detailed architecture diagram available in **agent_graph.md**

---

## 📂 Project Structure

├── run.py
├── config/config.yaml
├── src/
│ ├── agents/
│ ├── orchestrator/
│ ├── utils/
├── prompts/
├── data/
├── reports/
├── logs/
├── tests/
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate (Windows)


### 2️⃣ Install dependencies
pip install -r requirements.txt


---

## ▶️ Usage

### Main execution command (exact)
python run.py "Analyze ROAS drop" --data data/synthetic_fb_ads_undergarments.csv


### Output files generated automatically (no manual steps required)
| File | Description |
|------|-------------|
| `reports/insights.json` | Validated hypotheses with evidence & confidence |
| `reports/creatives.json` | Creative suggestions for low-CTR campaigns |
| `reports/report.md` | Final marketer-friendly report |
| `logs/run_logs.json` | Step-by-step trace of entire agent pipeline |

---

## 📍 Prompt-Driven Reasoning
Each agent uses structured LLM prompting stored in `/prompts/` with:
- JSON schema constraints
- Think → Analyze → Conclude reasoning
- Reflection logic for low confidence
- Modular & reusable design

---

## 🔁 Reproducibility / Deterministic Run
- All paths & thresholds are configured via `config/config.yaml`
- Same dataset + same config = same results
- No hidden memory / randomness

---

## 🧪 Tests
A basic evaluator unit test is included:
tests/test_evaluator.py


Run:
pytest


---

## 📌 Release & Review
| Requirement | Status |
|-------------|--------|
| v1.0 Release | ✔ Published |
| Self-review Pull Request | ✔ Created & describes design decisions |

Links can be added here (optional for reviewers):
- v1.0 Release: <paste link>
- Self-review PR: <paste link>

---

## 👨‍💻 Author
**Suryansh Tyagi**  
Applied AI Engineer — Assignment for Kasparro