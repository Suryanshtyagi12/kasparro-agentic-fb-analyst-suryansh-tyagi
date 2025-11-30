from src.utils.logger import log_event, log_error

class EvaluatorAgent:
    def validate(self, hypotheses, data_summary):
        try:
            log_event("evaluator_agent_start", {"hypothesis_count": len(hypotheses)})

            summary = data_summary.get("summary", {})
            results = []

            for h in hypotheses:
                hypothesis_text = h.get("hypothesis", h.get("statement", ""))
                metrics = h.get("metrics", {})

                confidence = 0.5
                evidence = {}

                ctr_before = metrics.get("ctr_before")
                ctr_after = metrics.get("ctr_after")

                if ctr_before is not None and ctr_after is not None:
                    delta = ctr_after - ctr_before
                    confidence = min(1.0, max(0.0, abs(delta) * 5))
                    evidence = {
                        "ctr_before": ctr_before,
                        "ctr_after": ctr_after,
                        "delta": delta,
                    }

                evidence["avg_ctr"] = summary.get("avg_ctr")

                results.append({
                    "id": h.get("id", ""),
                    "hypothesis": hypothesis_text,
                    "evidence": evidence,
                    "confidence": confidence
                })

            log_event("evaluator_agent_results", {"validated_count": len(results)})

            return results

        except Exception as e:
            log_error("evaluator_agent_error", e)
            raise
