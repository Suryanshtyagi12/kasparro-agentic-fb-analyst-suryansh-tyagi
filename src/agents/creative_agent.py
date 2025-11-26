class CreativeAgent:
    def generate_recommendations(self, data_summary):
        df = data_summary["df"]
        low_ctr = df[df["ctr"] < df["ctr"].quantile(0.25)]

        sample_messages = low_ctr["creative_message"].unique()[:3].tolist()

        return {
            "low_ctr_sample_messages": sample_messages,
            "recommendations": [
                {"headline": "Rediscover comfort — Feel the premium difference", "cta": "Shop Now"},
                {"headline": "Style + Comfort for everyday wear", "cta": "Explore Collection"},
                {"headline": "Because you deserve premium essentials", "cta": "Buy Now"},
            ]
        }
