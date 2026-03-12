---
name: agent-safety-net
description: Prevent common AI-agent failures in real work: context explosion, hidden stalls, weak memory continuity, noisy tool output, setup gaps, and poor observability. Use when the user wants to build, operate, debug, or improve an agent or agent workflow so it feels more reliable, cheaper, easier for beginners, and more production-ready.
---

# Agent Safety Net

Make agents feel usable in the real world, not just impressive in demos.

## Default workflow

1. Identify the pain point category.
2. Map the symptom to a likely root cause.
3. Apply the smallest useful safeguard.
4. Explain what problem the safeguard solves.
5. If needed, leave behind a reusable workflow, script, or operating rule.

## Pain points this skill covers

### 1. Context explosion
Solve when sessions get too long, too slow, too expensive, or repeatedly hit compaction issues.

Do this:
- summarize the active task into a small handoff file
- recommend or trigger session rollover
- keep only the minimum identifiers, blockers, and next step

Read: `references/context-and-session-maintenance.md`

### 2. Hidden stalls and reliability failures
Solve when the agent appears frozen, stops mid-task, loops, or waits invisibly for approval.

Do this:
- check whether the run is truly stuck or waiting on a prompt/permission
- surface the exact blocking point
- shorten the recovery path for the user

Read: `references/reliability-watchdog.md`

### 3. Weak memory continuity
Solve when the user has to repeat themselves across sessions, or when long tasks lose prior decisions.

Do this:
- preserve decisions, preferences, constraints, and current state
- separate raw logs from curated memory
- keep memory small and high-signal

Read: `references/memory-continuity.md`

### 4. Noisy tool output
Solve when MCP or tool output is too long, too structured, too repetitive, or too expensive to feed back into the model.

Do this:
- reduce tool payloads before giving them back to the model
- keep only the fields needed for the next decision
- prefer programmatic extraction over pasting giant blobs

Read: `references/tool-output-reduction.md`

### 5. Setup gap: installed but not usable
Solve when a tool is technically installed but still not working end to end.

Do this:
- verify the full chain, not just package presence
- check env vars, cookies, browsers, MCP endpoints, permissions, and login state
- leave behind a known-good checklist

Read: `references/setup-finisher.md`

### 6. Poor observability
Solve when the user cannot tell what the agent is doing, why it stopped, or where time/tokens are going.

Do this:
- report current stage, blocker, and next action clearly
- expose context pressure, retries, and failure reasons when possible
- prefer short human-readable status over raw logs

Read: `references/observability.md`

## Bundled scripts

- `scripts/make_active_task.py` — write a compact active-task handoff file
- `scripts/reduce_tool_output.py` — trim large JSON/tool payloads into compact summaries

## Output format

When helping the user, default to:
- pain point
- what is probably happening
- what to do now
- what reusable safeguard should be added

Keep it concrete and beginner-friendly.
