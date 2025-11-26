class EvaluatorAgent:
    def validate(self, hypotheses, data_summary):
        s = data_summary["summary"]
        results = []

        for h in hypotheses:
            if h["id"] == "H1":
                delta = s["latest_roas"] - s["previous_roas"]
                confidence = "high" if delta < -0.10 else "medium"
                evidence = f"ROAS change: {round(delta, 4)}"
            
            elif h["id"] == "H2":
                var = max(s["roas_by_campaign"].values()) - min(s["roas_by_campaign"].values())
                confidence = "high" if var > 0.5 else "medium"
                evidence = f"ROAS variance across campaigns: {round(var, 4)}"

            elif h["id"] == "H3":
                confidence = "medium"
                evidence = "Repeated creatives detected (trend not evaluated in depth)"

            results.append({
                "id": h["id"],
                "hypothesis": h["hypothesis"],
                "evidence": evidence,
                "confidence": confidence
            })

        return results
