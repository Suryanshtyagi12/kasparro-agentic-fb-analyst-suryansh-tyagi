class PlannerAgent:
    def create_plan(self, query):
        return {
            "query": query,
            "steps": ["load_data", "analyze_roas", "check_ctr", "evaluate_hypotheses"]
        }
