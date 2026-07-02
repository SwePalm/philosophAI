# PhilosophAI

**A personal philosophical companion for Claude: 17 philosophers, one router, and a journal that remembers.**

Daily check-ins, weekly reviews, and on-demand counsel — each session routed to the philosopher whose method actually fits the moment. Stressed about things you can't control? Seneca. Paralyzed by a big decision? Kierkegaard. Forcing an outcome that won't come? Lao Tzu. Everything you reflect on is distilled into a local markdown journal, so the companion gets to know you over time.

## Install

In [Claude Code](https://claude.com/claude-code) (CLI, desktop app, or IDE):

```
/plugin marketplace add SwePalm/philosophAI
/plugin install philosophai@swepalm
```

Then just talk to it — the skill triggers automatically on reflection-shaped requests, or invoke it directly:

```
/philosophai:reflect
```

First run takes ~30 seconds: it asks your name, what season of life you're in, and how you want to use it. That becomes your profile.

## Use it

- **"Quick check-in on my day"** → a daily reflection with whoever fits what happened
- **"Let's do my weekly review"** → a structured retrospective through one lens
- **"I'm anxious about the reorg at work"** → Seneca, on demand
- **"What would Nietzsche say about this?"** → any philosopher, by name
- **"Give me a council on this dilemma"** → 2–3 contrasting voices on a genuinely hard call
- **"Which lens should I use? How am I doing?"** → the Balance Coach analyzes your journal patterns

## The house of philosophers

| | | |
|---|---|---|
| **Socrates** questions everything | **Aristotle** builds character | **Epicurus** subtracts anxiety |
| **Seneca** separates what's yours | **Nagarjuna** dissolves fixed ideas | **Confucius** repairs relationships |
| **Lao Tzu** stops the forcing | **Montaigne** honors the ordinary | **Kant** tests your principles |
| **Mill** weighs the tradeoffs | **Kierkegaard** dignifies the dread | **Nietzsche** demands your greatness |
| **Dewey** designs the experiment | **Camus** rebels with joy | **de Beauvoir** exposes bad faith |
| **Nussbaum** decodes emotions | **bell hooks** makes love a practice | + the **Balance Coach** (meta) |

## Your journal

Everything lives in `~/.philosophai/` as plain markdown you own:

- `profile.md` — who you are, your values, current focus
- `journal.md` — dated, tagged entries capturing the essence of each session

It stays on your machine. Read it, edit it, back it up, grep it — it's yours. Each session begins by reading recent entries, so patterns surface over time ("three entries this month circle the same fear").

> **Note**: PhilosophAI is philosophical reflection, not therapy or mental-health care. If you're in crisis, please reach out to a professional or your local crisis line.

## How it works

One [Agent Skill](https://code.claude.com/docs/en/skills) with progressive disclosure:

- [`skills/reflect/SKILL.md`](skills/reflect/SKILL.md) — the control plane: session protocol (remember → route → embody → scribe), routing table, shared constraints
- [`skills/reflect/references/`](skills/reflect/references/) — an [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)-conformant knowledge bundle: one concept file per philosopher, plus the Scribe protocol and the Balance Coach

Only the router loads by default; the chosen philosopher's file is read on demand. Adding a philosopher = add one reference file + one row in the routing table + one line in [`references/index.md`](skills/reflect/references/index.md). PRs welcome.

## History

- **1.0** — multi-agent "teams" on Google ADK, driven from a notebook
- **2.0** — re-architected to unified skills + control plane ([`archive/PhilosophAI_2.0`](archive/PhilosophAI_2.0)), but the runtime was never built
- **3.0** (this) — the 2.0 architecture, running natively on Claude's Agent Skills: the runtime problem dissolved instead of solved

## License

MIT © Stefan Palm
