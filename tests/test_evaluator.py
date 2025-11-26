import pytest
from src.agents.evaluator_agent import EvaluatorAgent

def test_evaluator_validation():
    evaluator = EvaluatorAgent()

    hypotheses = [
        {
            "id": "H1",
            "hypothesis": "Test hypothesis",
            "expected_evidence": [],
        }
    ]

    data_summary = {
        "summary": {
            "roas_by_campaign": {"A": 3.0, "B": 5.0}
        }
    }

    result = evaluator.validate(hypotheses, data_summary)

    # Result should be a list with at least one item
    assert isinstance(result, list)
    assert len(result) >= 1

    # Each result must contain keys
    item = result[0]
    assert "id" in item
    assert "confidence" in item
    assert "validated" in item
