# PhilosophAI 2.0

This directory contains the re-architected "Control Plane + Skills" version of PhilosophAI.

## Structure

- **`AGENTS.md`**: The brain. Defines the Control Plane (Router) logic.
- **`main.py`**: The entry point. Initializes the agents and tools.
- **`data/memory.md`**: The persistent Markdown journal.
- **`skills/`**: The capabilities directory.
    - **`socrates/`**: The Inquisitor skill (Unified Mode).
    - **`balance_coach/`**: System diagnostics skill.
    - **`memory/`**: Tools for reading/writing `memory.md`.

## How to add a new Philosopher
1. Create `skills/<name>/SKILL.md`.
2. Define the Persona and Modes in that file.
3. Register the skill in `AGENTS.md` (so the router knows about it).
4. Register the agent in `main.py`.

## Evaluation
Use `evaluate.py` (to be implemented) to run the scenarios from `../the_teams/*_queries.json` against the new architecture.
