from src.utils.logger import log_event, log_error

class PlannerAgent:
    def create_plan(self, query):
        try:
            log_event("planner_start", {"query": query})

            plan = {
                "query": query,
                "steps": ["load_data", "analyze_roas", "check_ctr", "evaluate_hypotheses"]
            }

            log_event("planner_plan_created", {"plan": plan})

            return plan

        except Exception as e:
            log_error("planner_error", e)
            raise
