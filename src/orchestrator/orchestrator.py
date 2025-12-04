import yaml
import json
import os
import datetime

from src.agents.planner import PlannerAgent
from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.agents.creative_agent import CreativeAgent

from src.utils.logger import log_event, log_error


class Orchestrator:
    def __init__(self, config_path="config/config.yaml"):

        # --- Load config
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

        self.data_path = self.config.get("paths", {}).get(
            "data_path", "data/synthetic_fb_ads_undergarments.csv"
        )
        self.out_dir = self.config.get("paths", {}).get("out_dir", "reports")
        os.makedirs(self.out_dir, exist_ok=True)

        # --- Initialize agents
        self.planner = PlannerAgent()
        self.data_agent = DataAgent()
        self.insight_agent = InsightAgent()
        self.evaluator = EvaluatorAgent()
        self.creative = CreativeAgent()

    # --------------------------------------------------------
    # 🔥 V2: Per-Run Logging + Trace System
    # --------------------------------------------------------
    def _start_run(self, query):
        run_id = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")
        run_dir = os.path.join("logs", run_id)
        os.makedirs(run_dir, exist_ok=True)

        log_event("run_started", {"run_id": run_id, "query": query})

        def save_step(filename, payload):
            """Save JSON inside logs/<run_id>/"""
            with open(os.path.join(run_dir, filename), "w", encoding="utf-8") as f:
                json.dump(payload, f, indent=2, ensure_ascii=False)

        return run_id, run_dir, save_step

    # --------------------------------------------------------
    # 🔥 MAIN PIPELINE
    # --------------------------------------------------------
    def run(self, query):

        # --- Create run folder + save helper
        run_id, run_dir, save_step = self._start_run(query)

        trace = {"run_id": run_id, "steps": [], "status": "in_progress"}

        try:
            # ----------------- Planner -----------------
            plan = self.planner.create_plan(query)
            log_event("planner_completed", plan)
            save_step("planner.json", plan)
            trace["steps"].append("planner")

            # ----------------- Data Agent -----------------
            data_summary = self.data_agent.load_and_summarize(self.data_path)
            log_event("data_agent_completed", {"summary_keys": list(data_summary["summary"].keys())})
            save_step("data_summary.json", data_summary["summary"])
            trace["steps"].append("data_agent")

            # ----------------- Insight Agent -----------------
            hypotheses = self.insight_agent.generate_hypotheses(plan, data_summary)
            log_event("insight_agent_completed", {"count": len(hypotheses)})
            save_step("insights.json", hypotheses)
            trace["steps"].append("insight_agent")

            # ----------------- Evaluator Agent -----------------
            validated = self.evaluator.validate(hypotheses, data_summary)
            log_event("evaluation_completed", {"validated_count": len(validated)})
            save_step("evaluator.json", validated)
            trace["steps"].append("evaluator")

            # ----------------- Creative Agent -----------------
            creatives = self.creative.generate_recommendations(validated, data_summary)
            log_event("creative_agent_completed", {"count": len(creatives)})
            save_step("creatives.json", creatives)
            trace["steps"].append("creative_agent")

            # ----------------- MARK RUN COMPLETE -----------------
            trace["status"] = "completed"
            save_step("run_trace.json", trace)
            log_event("run_completed", trace)

        except Exception as e:
            trace["status"] = "failed"
            trace["error"] = str(e)
            save_step("run_trace.json", trace)
            log_error("run_failed", str(e))
            raise

        # ----------------- Write Report to reports/ -----------------
        report_path = os.path.join(self.out_dir, "report.md")
        insights_path = os.path.join(self.out_dir, "insights.json")
        creatives_path = os.path.join(self.out_dir, "creatives.json")

        with open(insights_path, "w", encoding="utf-8") as f:
            json.dump(validated, f, indent=2, ensure_ascii=False)

        with open(creatives_path, "w", encoding="utf-8") as f:
            json.dump(creatives, f, indent=2, ensure_ascii=False)

        summary = data_summary["summary"]

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("# 📌 Facebook Ads Performance Diagnosis Report\n\n")
            f.write("## 📈 ROAS & CTR Overview\n")
            f.write(f"- Average ROAS: **{summary.get('avg_roas')}**\n")
            f.write(f"- Latest ROAS: **{summary.get('latest_roas')}**\n")
            f.write(f"- Previous ROAS: **{summary.get('previous_roas')}**\n")
            f.write(f"- Average CTR: **{summary.get('avg_ctr')}%**\n")
            f.write(f"- ROAS Variance: **{summary.get('roas_variance')}**\n")
            f.write("\n### Agent Outputs Stored In: logs/{run_id}/\n")

        return {
            "run_id": run_id,
            "run_logs": run_dir,
            "insights": insights_path,
            "creatives": creatives_path,
            "report": report_path
        }
