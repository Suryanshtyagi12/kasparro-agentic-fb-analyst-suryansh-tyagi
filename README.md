
Kasparro – Agentic Facebook Performance Analyst

Author: Suryansh Tyagi
Version: v1.0

This project implements a fully autonomous multi-agent system that diagnoses Facebook Ads performance issues, identifies causes of ROAS decline, and generates data-driven creative recommendations.
It follows the assignment specification for Agentic Marketing Analysts and includes planner, data, insight, evaluator, and creative agents with logging, tests, structured JSON outputs, and reproducible execution.

🚀 1. Quick Start
1️⃣ Create virtual environment
python -V   # must be >= 3.10
python -m venv .venv
# Windows
.venv\Scripts\activate
# MacOS/Linux
source .venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run pipeline
python run.py "Analyze ROAS drop"

Optional: Run with config
python run.py "Analyze ROAS drop" --config config/config.yaml

📂 2. Repository Structure
kasparro-agentic-fb-analyst-suryansh-tyagi/
│
├── run.py
├── README.md
├── agent_graph.md
├── requirements.txt
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── synthetic_fb_ads_undergarments.csv
│   └── README.md
│
├── src/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── data_agent.py
│   │   ├── insight_agent.py
│   │   ├── evaluator_agent.py
│   │   └── creative_agent.py
│   │
│   ├── orchestrator/
│   │   └── orchestrator.py
│   │
│   └── utils/
│       └── logger.py
│
├── prompts/
│   ├── planner_prompt.md
│   ├── data_prompt.md
│   ├── insight_prompt.md
│   ├── evaluator_prompt.md
│   └── creative_prompt.md
│
├── reports/
│   ├── insights.json
│   ├── creatives.json
│   └── report.md
│
├── logs/
│   └── run_logs.json
│
└── tests/
    ├── test_data_agent.py
    ├── test_evaluator.py
    ├── test_pipeline.py
    └── conftest.py

⚙️ 3. Configuration

config/config.yaml controls thresholds, paths, seeds & analysis settings.

seed: 42

thresholds:
  low_ctr_pct: 0.10
  low_ctr_value: 0.005
  roas_drop_pct: 0.20

analysis:
  lookback_days: 28
  compare_window_days: 14

=======
Kasparro – Agentic Facebook Performance Analyst

Author: Suryansh Tyagi
Version: v1.0

This project implements a fully autonomous multi-agent system that diagnoses Facebook Ads performance issues, identifies causes of ROAS decline, and generates data-driven creative recommendations.
It follows the assignment specification for Agentic Marketing Analysts and includes planner, data, insight, evaluator, and creative agents with logging, tests, structured JSON outputs, and reproducible execution.

🚀 1. Quick Start
1️⃣ Create virtual environment
python -V   # must be >= 3.10
python -m venv .venv
# Windows
.venv\Scripts\activate
# MacOS/Linux
source .venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run pipeline
python run.py "Analyze ROAS drop"

Optional: Run with config
python run.py "Analyze ROAS drop" --config config/config.yaml

📂 2. Repository Structure
kasparro-agentic-fb-analyst-suryansh-tyagi/
│
├── run.py
├── README.md
├── agent_graph.md
├── requirements.txt
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── synthetic_fb_ads_undergarments.csv
│   └── README.md
│
├── src/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── data_agent.py
│   │   ├── insight_agent.py
│   │   ├── evaluator_agent.py
│   │   └── creative_agent.py
│   │
│   ├── orchestrator/
│   │   └── orchestrator.py
│   │
│   └── utils/
│       └── logger.py
│
├── prompts/
│   ├── planner_prompt.md
│   ├── data_prompt.md
│   ├── insight_prompt.md
│   ├── evaluator_prompt.md
│   └── creative_prompt.md
│
├── reports/
│   ├── insights.json
│   ├── creatives.json
│   └── report.md
│
├── logs/
│   └── run_logs.json
│
└── tests/
    ├── test_data_agent.py
    ├── test_evaluator.py
    ├── test_pipeline.py
    └── conftest.py

⚙️ 3. Configuration

config/config.yaml controls thresholds, paths, seeds & analysis settings.

seed: 42

thresholds:
  low_ctr_pct: 0.10
  low_ctr_value: 0.005
  roas_drop_pct: 0.20

analysis:
  lookback_days: 28
  compare_window_days: 14

>>>>>>> review
paths:
  data_path: data/synthetic_fb_ads_undergarments.csv
  out_dir: reports

🧠 4. Architecture Overview

This system follows Kasparro’s Agentic Reasoning Loop.

🔹 Planner Agent

Breaks the user query into structured subtasks.

🔹 Data Agent

Loads the dataset, validates structure, computes ROAS/CTR summaries, and extracts campaign-level patterns.

🔹 Insight Agent

Generates hypotheses about performance issues:

CTR decline

ROAS volatility

Creative fatigue

Campaign underperformance

🔹 Evaluator Agent

Quantitatively validates hypotheses:

CTR difference

ROAS change

Variance across campaigns

Confidence scoring (0–1)

🔹 Creative Agent

Generates new creative ideas based on:

Low CTR campaigns

Most common messaging patterns

Observed themes in data

🔹 Orchestrator

Orchestrates all agents:

calls agents in order

logs events

handles errors

writes outputs

See detailed flow diagram in agent_graph.md.

📈 5. Example Outputs
insights.json
[
  {
    "id": "H1",
    "hypothesis": "ROAS dropped recently — CTR decline may be the reason",
    "evidence": {
      "ctr_before": 0.08,
      "ctr_after": 0.04,
      "delta": -0.04,
      "avg_ctr": 7.12
    },
    "confidence": 0.8
  }
]

creatives.json
{
  "low_ctr_sample_messages": [
    "Buy 1 Get 1",
    "Comfort-first cotton"
  ],
  "recommendations": [
    {
      "headline": "Rediscover comfort — Feel the premium difference",
      "cta": "Shop Now"
    }
  ]
}

report.md

Contains ROAS/CTR summary + insights + creative recommendations.

🛰 6. Logging & Observability

All events are logged in:

logs/run_logs.json


Each log entry is structured JSON:

{
  "timestamp": "2025-11-30T11:12:00Z",
  "event": "insight_agent_hypotheses_generated",
  "level": "INFO",
  "details": {"count": 3}
}


This helps debugging and traceability.

🧪 7. Testing

Run all tests:

pytest -q


The test suite includes:

Evaluator tests

DataAgent tests

Full pipeline integration tests

All tests must pass.

🏷 8. Git Hygiene

To meet Kasparro’s submission standards:

✔ Multiple meaningful commits

Example:

git add .
git commit -m "Add evaluator tests + fixed metric logic"
git commit -m "Implement structured logging and tracing"
git commit -m "Improve README and config"

✔ v1.0 Release Tag
git tag -a v1.0 -m "Initial stable release"
git push --tags

✔ Self-Review PR

Create a PR titled "self-review" with:

Architecture decisions

Prompting strategy

Validation method

Logging design

Example outputs

Limitations & improvements

🎯 9. Evaluation Checklist (All Completed)

 README includes setup, usage, architecture, examples

 config.yaml included

 Proper agentic architecture

 Prompts in separate files

 reports/ populated

 logs/ populated

 tests/ included and passing

 v1.0 release tag

 self-review PR
