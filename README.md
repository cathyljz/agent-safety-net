# Agent Safety Net

Make AI agents feel **stable, cheaper, easier to understand, and easier for beginners to use**.

This is an AgentSkill inspired by real user pain from public agent tools and framework discussions.
It focuses on the unglamorous problems that make agents frustrating in real work:

- sessions getting longer and worse over time
- agents freezing or looking stuck
- tools returning giant noisy payloads
- memory across sessions being weak
- installs that look finished but still do not work
- users not knowing what the agent is doing right now

## What this skill actually does

`agent-safety-net` helps an AI agent diagnose and improve **operational pain**, not just generate output.

It gives the agent a practical playbook for six common failures:

### 1. Context explosion
**Problem:** the session gets too long, too slow, too expensive, or starts failing compaction.

**What this skill teaches:**
- shrink the current task into a compact handoff
- preserve only the important state
- continue in a clean session instead of dragging the whole history forward

**Why this matters:**
Users feel this as “it got dumber and slower the longer we talked.”

---

### 2. Hidden stalls and reliability failures
**Problem:** the agent looks frozen, stops in the middle, or silently waits for approval.

**What this skill teaches:**
- check whether the agent is actually blocked on permission/input
- identify the last successful step
- tell the user the blocker in plain language

**Why this matters:**
Users usually say “it froze.” Often the real issue is invisible waiting, retries, or a stuck tool.

---

### 3. Weak memory continuity
**Problem:** users repeat preferences and prior decisions again and again.

**What this skill teaches:**
- separate durable memory from current-task state
- store only the parts that help future execution
- avoid dumping entire conversations into memory

**Why this matters:**
A useful agent should feel cumulative, not stateless.

---

### 4. Noisy tool output
**Problem:** tools return giant JSON blobs, repeated metadata, and long logs that waste context.

**What this skill teaches:**
- reduce tool payloads before handing them back to the model
- keep only the fields needed for the next decision
- use deterministic extraction where possible

**Why this matters:**
This directly affects quality, speed, and token cost.

---

### 5. Setup gap: installed but not usable
**Problem:** something is “installed” but still fails in real use.

**What this skill teaches:**
- verify the whole chain, not just package presence
- check auth, browser dependencies, env vars, MCP endpoints, cookies, and permissions
- treat setup as done only when a real action works

**Why this matters:**
Beginners think “installed” means “ready.” Good agent tooling should close that gap.

---

### 6. Poor observability
**Problem:** the user cannot tell what the agent is doing, why it stopped, or what happens next.

**What this skill teaches:**
- give short status updates with stage, blocker, and next action
- prefer human-readable status over dense raw traces

**Why this matters:**
Good observability turns a confusing agent into a dependable one.

## Who this is for

This skill is useful if you are:
- building an AI agent product
- running OpenClaw / Codex / Claude Code / AutoGen style workflows
- debugging long-running agent sessions
- trying to make agents easier for non-technical users
- designing a better “agent UX” instead of only adding more tools

## Files

- `SKILL.md` — trigger description + operating workflow
- `references/` — beginner-friendly explanations for each pain point and solution area
- `scripts/make_active_task.py` — generate a compact handoff summary for session rollover
- `scripts/reduce_tool_output.py` — reduce large JSON/tool payloads

## Example use cases

- “This session is getting huge. Help me keep it usable.”
- “The agent looks stuck. Figure out whether it is actually blocked.”
- “This MCP output is too verbose. Reduce it before reasoning.”
- “The install says success, but the tool still does not work. Check the whole chain.”
- “Help me make my agent product feel more stable for beginners.”

## Why this repo exists

Most agent demos focus on what agents **can do**.
This skill focuses on why agents often feel bad to use in real life — and what to do about it.

That makes it a good fit for anyone working on:
- agent reliability
- agent UX
- token efficiency
- session maintenance
- operator confidence
- beginner-friendly automation
