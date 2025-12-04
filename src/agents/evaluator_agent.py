# src/agents/evaluator_agent.py
from math import log1p
from src.utils.logger import log_event, log_error

def score_confidence(delta_abs, baseline, scale=0.5):
    # simple logistic-like monotonic mapping in [0,1]
    # delta_abs is absolute change in metric (e.g., 0.03 for CTR 3%)
    # baseline is baseline metric value
    if baseline is None or baseline == 0:
        return min(1.0, delta_abs * 10)  # fall back
    rel = delta_abs / (baseline + 1e-9)
    # map relative change to [0,1] loosely
    return float(max(0.0, min(1.0, (rel*scale) / (1 + rel*scale))))

class EvaluatorAgent:
    def validate(self, hypotheses, data_summary):
        results = []
        s = data_summary.get("summary", {})
        for h in hypotheses:
            try:
                metric = h.get("metric")  # e.g., 'ctr' or compound
                segment = h.get("segment")  # optional target segment
                evidence = {}
                confidence = 0.5
                impact = "medium"

                # Example: if h provides before/after numbers already, use them
                if "metrics" in h and "before" in h["metrics"] and "after" in h["metrics"]:
                    before = h["metrics"]["before"]
                    after = h["metrics"]["after"]
                    delta = after - before
                    pct = (delta / (before + 1e-9)) * 100
                    evidence = {"before": before, "after": after, "delta": delta, "delta_pct": round(pct,2)}
                    confidence = score_confidence(abs(delta), abs(before))
                    # impact rules (example)
                    if abs(pct) > 30:
                        impact = "high"
                    elif abs(pct) > 10:
                        impact = "medium"
                    else:
                        impact = "low"
                else:
                    # fallback: compute segment aggregates from data_summary (agg DF)
                    agg = data_summary.get("agg")  # ensure your data_agent creates weekly/campaign agg
                    # h should contain a selector; implement safe lookup...
                    # For simplicity, mark low-confidence fallback
                    evidence = {"note":"no direct metrics provided"}
                    confidence = 0.4

                results.append({
                    "id": h.get("id"),
                    "hypothesis": h.get("hypothesis"),
                    "metric": metric,
                    "segment": segment,
                    "evidence": evidence,
                    "impact": impact,
                    "confidence": round(confidence, 2)
                })
            except Exception as e:
                log_error("evaluator_exception", e)
                results.append({
                    "id": h.get("id"),
                    "hypothesis": h.get("hypothesis"),
                    "evidence": {"error": str(e)},
                    "impact": "unknown",
                    "confidence": 0.0
                })
        log_event("evaluator_completed", {"count": len(results)})
        return results
