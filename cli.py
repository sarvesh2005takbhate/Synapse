# cli.py
import argparse, json, os
from agents.agent_runner import run_scenario_text

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", required=True, help="path to scenario json")
    args = parser.parse_args()
    with open(args.scenario, "r", encoding="utf-8") as f:
        data = json.load(f)
    desc = data.get("description") or json.dumps(data)
    result = run_scenario_text(desc)
    print("=== TRACE ===")
    print(result["trace"])
    print("\n=== FINAL PLAN ===")
    print(result["final_plan"])
    # write log
    os.makedirs("logs", exist_ok=True)
    sid = data.get("id", "scenario")
    with open(f"logs/{sid}.json", "w", encoding="utf-8") as out:
        json.dump(result, out, indent=2)

if __name__ == "__main__":
    main()
