from src.utils.logger import log_event, log_error

class CreativeAgent:
    def generate_recommendations(self, validated_hypotheses, data_summary, top_k=3):
        out = []
        for v in validated_hypotheses:
            if v["confidence"] < 0.4:
                continue
            seg = v.get("segment", {})
            metric = v.get("metric")
            reason = v.get("evidence", {})
            # Example template mapping:
            if metric == "ctr":
                headline = f"See why {seg.get('campaign','this campaign')} is getting attention — Explore now"
                body = f"CTR dropped by {reason.get('delta_pct','N/A')}% for {seg.get('campaign','the campaign')}. Try benefit-focused creative and social proof."
                out.append({"campaign": seg.get("campaign"), "headline": headline, "body": body, "cta":"Shop Now"})
            else:
                out.append({"campaign": seg.get("campaign"), "headline":"Try this headline", "body":"Sample", "cta":"Learn More"})
        log_event("creative_generated", {"count": len(out)})
        return out
