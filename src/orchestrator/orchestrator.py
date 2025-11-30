import yaml
import json
import os
from src.agents.planner import PlannerAgent
from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.agents.creative_agent import CreativeAgent
from src.utils.logger import log_event

class Orchestrator:
    def __init__(self, config_path="config/config.yaml"):
        # Load config
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

        # Extract paths from config (with defaults)
        self.data_path = self.config.get("paths", {}).get("data_path", "data/synthetic_fb_ads_undergarments.csv")
        self.out_dir = self.config.get("paths", {}).get("out_dir", "reports")

        # Ensure output directory exists
        os.makedirs(self.out_dir, exist_ok=True)

        # Initialize agents
        self.planner = PlannerAgent()
        self.data_agent = DataAgent()
        self.insight_agent = InsightAgent()
        self.evaluator = EvaluatorAgent()
        self.creative = CreativeAgent()
        self.log_event = log_event

    def run(self, query):
        # --- Planner ---
        plan = self.planner.create_plan(query)
        try:
            self.log_event("plan_created", plan)
        except Exception:
            pass

        # --- Data Agent ---
        data_summary = self.data_agent.load_and_summarize(self.data_path)
        try:
            self.log_event("data_summary", data_summary.get("summary", {}))
        except Exception:
            pass

        # --- Insight Agent ---
        hypotheses = self.insight_agent.generate_hypotheses(plan, data_summary)
        try:
            self.log_event("hypotheses_generated", hypotheses)
        except Exception:
            pass

        # --- Evaluator ---
        validated = self.evaluator.validate(hypotheses, data_summary)
        try:
            self.log_event("validation_results", validated)
        except Exception:
            pass

        # --- Creative Agent ---
        creatives = self.creative.generate_recommendations(data_summary)
        try:
            self.log_event("creatives_generated", creatives)
        except Exception:
            pass

        # --- Save Outputs ---
        insights_path = os.path.join(self.out_dir, "insights.json")
        creatives_path = os.path.join(self.out_dir, "creatives.json")
        report_path = os.path.join(self.out_dir, "report.md")

        with open(insights_path, "w", encoding="utf-8") as f:
            json.dump(validated, f, indent=2, ensure_ascii=False)

        with open(creatives_path, "w", encoding="utf-8") as f:
            json.dump(creatives, f, indent=2, ensure_ascii=False)

        # --- Report ---
        summary = data_summary.get("summary", {})
        avg_roas = summary.get("avg_roas", "N/A")
        latest_roas = summary.get("latest_roas", "N/A")
        previous_roas = summary.get("previous_roas", "N/A")
        avg_ctr = summary.get("avg_ctr", "N/A")
        roas_variance = summary.get("roas_variance", "N/A")

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("# 📌 Facebook Ads Performance Diagnosis Report\n\n")
            f.write("## 📈 ROAS & CTR Overview\n")
            f.write(f"- Average ROAS: **{avg_roas}**\n")
            f.write(f"- Latest ROAS: **{latest_roas}**\n")
            f.write(f"- Previous ROAS: **{previous_roas}**\n")
            f.write(f"- Average CTR: **{avg_ctr}%**\n")
            f.write(f"- ROAS Variance: **{roas_variance}**\n\n")
            f.write("### Full insights in insights.json\n")
            f.write("### Creative ideas in creatives.json\n")

        return {
            "insights": insights_path,
            "creatives": creatives_path,
            "report": report_path
        }
