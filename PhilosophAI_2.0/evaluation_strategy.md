# Evaluation Strategy: PhilosophAI 2.0

## Overview
The goal of this evaluation is to ensure that the new Unified Skill architecture (PhilosophAI 2.0) maintains or improves upon the performance of the original system while reducing complexity.

## 1. Regression Testing (Using Legacy Queries)
The original project contains `*_queries.json` files for each "team":
- `the_teams/daily_queries.json`
- `the_teams/weekly_queries.json`
- `the_teams/long_term_queries.json`
- `the_teams/on_demand_queries.json`

### Test Case Execution
An `evaluate.py` script will be used to:
1.  Load all legacy queries.
2.  Pass the query to the **Control Plane** (`AGENTS.md`).
3.  **Expected Outcome**: The Control Plane should route the query to the correct Unified Skill with the appropriate `task_mode`.
    - *Mapping Example*: A query from `daily_queries.json` originally intended for `Socrates` should now be routed to `skills/socrates` with `task_mode="daily_log"`.

## 2. Evaluation Metrics
- **Routing Accuracy**: Does the Control Plane select the correct philosopher?
- **Mode Selection**: Does it specify the correct task mode (Daily vs Weekly vs On-Demand)?
- **Response Quality**: Does the unified philosopher maintain the correct persona traits for that specific mode?

## 3. Automation
Run the evaluation script after any changes to `AGENTS.md` or any `SKILL.md` to ensure no regressions in routing logic.
