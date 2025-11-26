#!/usr/bin/env python3
import argparse
from src.orchestrator.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(description="Kasparro Agentic FB Analyst")
    parser.add_argument("query", type=str, help="e.g. 'Analyze ROAS drop'")
    parser.add_argument("--data", default="data/sample.csv")
    parser.add_argument("--out", default="reports")
    args = parser.parse_args()

    orchestrator = Orchestrator(config_path="config/config.yaml")
    orchestrator.run(query=args.query, data_path=args.data, out_dir=args.out)
    print("\n✓ Analysis complete — See results inside reports/ folder\n")

if __name__ == "__main__":
    main()
