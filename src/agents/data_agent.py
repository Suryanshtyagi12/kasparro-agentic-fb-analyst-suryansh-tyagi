import pandas as pd
from src.utils.logger import log_event, log_error

class DataAgent:
    def load_and_summarize(self, data_path):
        try:
            log_event("data_agent_loading_start", {"data_path": data_path})

            df = pd.read_csv(data_path)

            if "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"])
                df = df.sort_values("date")

            summary = {
                "avg_roas": round(df["roas"].mean(), 2),
                "avg_ctr": round(df["ctr"].mean() * 100, 2),
                "latest_roas": round(df.iloc[-1]["roas"], 2),
                "previous_roas": round(df.iloc[-2]["roas"], 2),
                "roas_variance": round(df["roas"].var(), 2),
                "roas_by_campaign": df.groupby("campaign_name")["roas"].mean().to_dict(),
                "top_campaigns": df.groupby("campaign_name")["roas"].mean().sort_values(ascending=False).head(3).to_dict(),
                "bottom_campaigns": df.groupby("campaign_name")["roas"].mean().sort_values().head(3).to_dict(),
            }

            log_event("data_agent_summary_created", {"summary": summary})

            return {"df": df, "summary": summary}

        except Exception as e:
            log_error("data_agent_error", e)
            raise
