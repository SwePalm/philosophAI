import json
import os
from pathlib import Path

def load_legacy_queries(base_path: Path):
    queries = {}
    teams = ["daily", "weekly", "long_term", "on_demand"]
    for team in teams:
        query_file = base_path / "the_teams" / f"{team}_queries.json"
        if query_file.exists():
            with open(query_file, 'r') as f:
                queries[team] = json.load(f)
    return queries

def run_evaluation_dry_run():
    """
    Simulates the evaluation by matching legacy query categories to new skills/modes.
    """
    legacy_root = Path("../") # Assuming evaluate.py is in PhilosophAI_2.0/
    queries = load_legacy_queries(legacy_root)
    
    print("=== PhilosophAI 2.0 Evaluation Report (Dry Run) ===")
    print(f"Loaded {sum(len(v) for v in queries.values())} legacy queries.\n")
    
    for team, cases in queries.items():
        print(f"--- Team: {team.upper()} ---")
        for agent_name, query_text in cases.items():
            # In the 2.0 architecture, we map these to skills/modes
            target_skill = agent_name.lower()
            
            # Map legacy teams to new modes
            mode_map = {
                "daily": "daily_log",
                "weekly": "weekly_review",
                "long_term": "long_term_vision",
                "on_demand": "on_demand"
            }
            target_mode = mode_map.get(team, "unknown")
            
            print(f"[ Legacy: {agent_name} ] -> [ New: skills/{target_skill} | mode: {target_mode} ]")
            print(f"  Query: \"{query_text[:60]}...\"")
        print()

if __name__ == "__main__":
    # In a real environment, you would use the ADK to actually invoke the agents:
    # from main import create_control_plane_agent
    # agent = create_control_plane_agent(llm, skills)
    # result = agent.run(query)
    
    run_evaluation_dry_run()
