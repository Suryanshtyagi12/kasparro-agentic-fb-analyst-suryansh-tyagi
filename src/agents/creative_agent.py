from src.utils.logger import log_event, log_error

class CreativeAgent:
    def generate_recommendations(self, data_summary):
        try:
            log_event("creative_agent_start", {})

            df = data_summary["df"]
            low_ctr = df[df["ctr"] < df["ctr"].quantile(0.25)]

            sample_messages = low_ctr["creative_message"].unique()[:3].tolist()

            output = {
                "low_ctr_sample_messages": sample_messages,
                "recommendations": [
                    {"headline": "Rediscover comfort — Feel the premium difference", "cta": "Shop Now"},
                    {"headline": "Style + Comfort for everyday wear", "cta": "Explore Collection"},
                    {"headline": "Because you deserve premium essentials", "cta": "Buy Now"},
                ]
            }

            log_event("creative_agent_output_created", {"messages_used": sample_messages})

            return output

        except Exception as e:
            log_error("creative_agent_error", e)
            raise
