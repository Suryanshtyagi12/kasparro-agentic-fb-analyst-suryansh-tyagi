class Orchestrator:
    def __init__(self, config_path):
        from src.agents.planner import PlannerAgent
        from src.agents.data_agent import DataAgent
        from src.agents.insight_agent import InsightAgent
        from src.agents.evaluator_agent import EvaluatorAgent
        from src.agents.creative_agent import CreativeAgent
        from src.utils.logger import log_event

        self.planner = PlannerAgent()
        self.data_agent = DataAgent()
        self.insight_agent = InsightAgent()
        self.evaluator = EvaluatorAgent()
        self.creative = CreativeAgent()
        self.log_event = log_event

    def run(self, query, data_path, out_dir):
        plan = self.planner.create_plan(query)
        self.log_event("plan_created", plan)

        data_summary = self.data_agent.load_and_summarize(data_path)
        self.log_event("data_summary", data_summary["summary"])

        hypotheses = self.insight_agent.generate_hypotheses(plan, data_summary)
        self.log_event("hypotheses_generated", hypotheses)

        validated = self.evaluator.validate(hypotheses, data_summary)
        self.log_event("validation_results", validated)

        creatives = self.creative.generate_recommendations(data_summary)
        self.log_event("creatives_generated", creatives)

        import json
        with open(f"{out_dir}/insights.json", "w") as f:
            json.dump(validated, f, indent=2)

        with open(f"{out_dir}/creatives.json", "w") as f:
            json.dump(creatives, f, indent=2)
        
        with open(f"{out_dir}/report.md", "w", encoding="utf-8") as f:
            f.write("# 📌 Facebook Ads Performance Diagnosis Report\n\n")
            f.write("## 📈 ROAS & CTR Overview\n")
            f.write(f"- Average ROAS: **{data_summary['summary']['avg_roas']}**\n")
            f.write(f"- Latest ROAS: **{data_summary['summary']['latest_roas']}**\n")
            f.write(f"- Previous ROAS: **{data_summary['summary']['previous_roas']}**\n")
            f.write(f"- Average CTR: **{data_summary['summary']['avg_ctr']}%**\n")
            f.write(f"- ROAS Variance: **{data_summary['summary']['roas_variance']}**\n\n")
            f.write("### Full insights in insights.json\n")
            f.write("### Creative ideas in creatives.json\n")

