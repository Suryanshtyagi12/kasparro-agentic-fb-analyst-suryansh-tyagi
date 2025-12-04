import pandas as pd
from src.utils.logger import log_event, log_error
from src.utils.schema_validator import validate_and_normalize, SchemaValidationError

class DataAgent:

    def load_and_summarize(self, data_path):
        try:
            log_event("data_agent_loading_start", {"data_path": data_path})

            # Load CSV
            df = pd.read_csv(data_path)

            # Schema validation + normalization
            try:
                df = validate_and_normalize(df)
                log_event("data_agent_schema_valid", {"rows": len(df)})
            except SchemaValidationError as e:
                log_error("schema_validation_failed", str(e))
                raise

            # Convert dates
            if "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"], errors="coerce")
                df = df.sort_values("date")

            # Compute summary safely
            summary = {
                "avg_roas": round(df["roas"].mean(), 4),
                "avg_ctr": round(df["ctr"].mean() * 100, 4),
                "latest_roas": round(df.iloc[-1]["roas"], 4),
                "previous_roas": round(df.iloc[-2]["roas"], 4),
                "roas_variance": round(df["roas"].var(), 4),
                "roas_by_campaign": df.groupby("campaign_name")["roas"].mean().round(4).to_dict(),
                "top_campaigns": df.groupby("campaign_name")["roas"].mean().sort_values(ascending=False).head(3).round(4).to_dict(),
                "bottom_campaigns": df.groupby("campaign_name")["roas"].mean().sort_values().head(3).round(4).to_dict(),
            }

            log_event("data_agent_summary_created", {"summary_keys": list(summary.keys())})

            return {"df": df, "summary": summary}

        except Exception as e:
            log_error("data_agent_error", str(e))
            raise
