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

        with open(f"{out_dir}/report.md", "w") as f:
            f.write("# Marketing Insights Report\n\n")
            f.write("## Summary\nInsights are saved in insights.json\n")
            f.write("\n## Creative Suggestions\nSee creatives.json\n")
