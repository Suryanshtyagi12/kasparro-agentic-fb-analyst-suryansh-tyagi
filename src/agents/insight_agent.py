class InsightAgent:
    def generate_hypotheses(self, plan, data_summary):
        s = data_summary["summary"]
        hypotheses = []

        # Hypothesis 1: ROAS drop due to CTR decline
        if s["latest_roas"] < s["previous_roas"]:
            hypotheses.append({
                "id": "H1",
                "hypothesis": "ROAS dropped recently — CTR decline may be the reason",
                "metric": "ctr"
            })

        # Hypothesis 2: Some campaigns performed worse than others
        hypotheses.append({
            "id": "H2",
            "hypothesis": "Some campaigns underperformed vs others (ROAS variance)",
            "metric": "roas_campaign"
        })

        # Hypothesis 3: Creative messaging fatigue
        hypotheses.append({
            "id": "H3",
            "hypothesis": "Creative fatigue — audience might be tired of repeated creatives",
            "metric": "creative_fatigue"
        })

        return hypotheses
