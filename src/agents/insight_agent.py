from src.utils.logger import log_event, log_error

class InsightAgent:
    def generate_hypotheses(self, plan, data_summary):
        try:
            log_event("insight_agent_start", {"plan": plan})

            s = data_summary["summary"]
            hypotheses = []

            if s["latest_roas"] < s["previous_roas"]:
                hypotheses.append({
                    "id": "H1",
                    "hypothesis": "ROAS dropped recently — CTR decline may be the reason",
                    "metric": "ctr"
                })

            hypotheses.append({
                "id": "H2",
                "hypothesis": "Some campaigns underperformed vs others (ROAS variance)",
                "metric": "roas_campaign"
            })

            hypotheses.append({
                "id": "H3",
                "hypothesis": "Creative fatigue — audience might be tired of repeated creatives",
                "metric": "creative_fatigue"
            })

            log_event("insight_agent_hypotheses_generated", {"count": len(hypotheses)})

            return hypotheses

        except Exception as e:
            log_error("insight_agent_error", e)
            raise
