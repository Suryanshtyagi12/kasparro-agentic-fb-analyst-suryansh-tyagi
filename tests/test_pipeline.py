from src.orchestrator.orchestrator import Orchestrator

def test_full_pipeline():
    orch = Orchestrator("config/config.yaml")
    outputs = orch.run("Analyze ROAS drop")

    assert "insights.json" in outputs["insights"]
    assert "creatives.json" in outputs["creatives"]
    assert "report.md" in outputs["report"]
