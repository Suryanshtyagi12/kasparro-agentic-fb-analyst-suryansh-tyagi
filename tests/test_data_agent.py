import pandas as pd
from src.agents.data_agent import DataAgent

def test_data_agent_summary():
    agent = DataAgent()
    summary = agent.load_and_summarize("data/synthetic_fb_ads_undergarments.csv")

    assert "summary" in summary
    assert "avg_roas" in summary["summary"]
    assert summary["summary"]["avg_roas"] >= 0
