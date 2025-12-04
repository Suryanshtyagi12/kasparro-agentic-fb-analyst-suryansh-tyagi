# src/agents/insight_agent.py
from src.utils.logger import log_event, log_error
import pandas as pd

class InsightAgent:
    def generate_hypotheses(self, plan, data_summary, lookback_weeks=4, compare_weeks=2):
        log_event("insight_start", {"plan": plan})
        df = data_summary["df"]  # raw df with date
        # compute week start or rolling window aggregator
        df["week"] = df["date"].dt.to_period("W").apply(lambda r: r.start_time)
        # define windows: baseline = last lookback_weeks excluding compare window
        weeks = sorted(df["week"].unique())
        if len(weeks) < (lookback_weeks + compare_weeks):
            # fallback: use earliest vs latest
            baseline_df = df.iloc[:max(1, len(df)//2)]
            current_df = df.iloc[max(1, len(df)//2):]
        else:
            current_weeks = weeks[-compare_weeks:]
            baseline_weeks = weeks[-(lookback_weeks+compare_weeks):-compare_weeks]
            baseline_df = df[df["week"].isin(baseline_weeks)]
            current_df = df[df["week"].isin(current_weeks)]

        hypotheses = []
        # example: detect CTR change by campaign
        grouped_base = baseline_df.groupby("campaign_name").agg({"clicks":"sum","impressions":"sum"})
        grouped_cur = current_df.groupby("campaign_name").agg({"clicks":"sum","impressions":"sum"})
        for campaign in set(grouped_base.index).union(grouped_cur.index):
            b = grouped_base.loc[campaign] if campaign in grouped_base.index else {"clicks":0,"impressions":0}
            c = grouped_cur.loc[campaign] if campaign in grouped_cur.index else {"clicks":0,"impressions":0}
            b_ctr = (b["clicks"]/b["impressions"]) if b["impressions"]>0 else 0
            c_ctr = (c["clicks"]/c["impressions"]) if c["impressions"]>0 else 0
            delta_pct = 0 if b_ctr==0 else ((c_ctr - b_ctr)/b_ctr)*100
            if abs(delta_pct) > 5:  # candidate threshold, make configurable
                hypotheses.append({
                    "id": f"H_ctr_{campaign}",
                    "hypothesis": f"CTR changed for campaign {campaign}",
                    "metric": "ctr",
                    "segment": {"campaign": campaign},
                    "metrics": {"before": round(b_ctr,4), "after": round(c_ctr,4), "delta_pct": round(delta_pct,2)}
                })
        # add campaign-level roas checks and creative repetition checks similarly
        log_event("insight_generated", {"count": len(hypotheses)})
        return hypotheses
