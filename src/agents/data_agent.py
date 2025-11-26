import pandas as pd

class DataAgent:
    def load_and_summarize(self, data_path):
        df = pd.read_csv(data_path)

        # Convert date column if exists
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
            "raw": df.to_dict(orient="records")
}

        return {"df": df, "summary": summary}
