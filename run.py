import argparse
from src.orchestrator.orchestrator import Orchestrator


def main():
    parser = argparse.ArgumentParser(description="Kasparro Agentic FB Analyst CLI")
    parser.add_argument("query", type=str, help="Enter query like: 'Analyze ROAS drop'")
    parser.add_argument("--config", type=str, default="config/config.yaml", help="Path to config.yaml")
    args = parser.parse_args()

    orch = Orchestrator(config_path=args.config)
    outputs = orch.run(args.query)

    print("\n🔥 Run completed successfully!")
    print("📄 Insights:", outputs["insights"])
    print("🎨 Creatives:", outputs["creatives"])
    print("📊 Report:", outputs["report"])

if __name__ == "__main__":
    main()

