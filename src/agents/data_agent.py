import pandas as pd

class DataAgent:
    def load_and_summarize(self, path):
        df = pd.read_csv(path)

        df['date'] = pd.to_datetime(df['date'])

        summary = {
            "avg_ctr": float(df["ctr"].mean()),
            "avg_roas": float(df["roas"].mean()),
            "roas_by_date": df.groupby("date")["roas"].mean().to_dict(),
            "ctr_by_date": df.groupby("date")["ctr"].mean().to_dict(),
            "roas_by_campaign": df.groupby("campaign_name")["roas"].mean().to_dict(),
            "ctr_by_campaign": df.groupby("campaign_name")["ctr"].mean().to_dict(),
            "latest_roas": float(df[df["date"] == df["date"].max()]["roas"].mean()),
            "previous_roas": float(df[df["date"] == df["date"].nlargest(2).iloc[-1]]["roas"].mean()),
        }

        return {"df": df, "summary": summary}
