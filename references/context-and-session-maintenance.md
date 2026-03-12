# Context and session maintenance

## What problem this solves
When an agent session grows too large, quality drops:
- responses get slower
- compaction can fail
- important details become harder to keep stable
- token cost becomes unpredictable

## Practical fix
Use a rollover pattern:
1. write a compact active-task summary
2. preserve only goal, constraints, current status, important ids/paths/errors, and next step
3. continue in a fresh session with the summary instead of the whole chat history

## Good safeguard
Trigger this automatically when:
- context is obviously large
- the agent repeats itself
- tool calls start looping
- compaction fails
- latency becomes noticeably worse

## Why beginners care
The user does not need to understand token accounting. They just need the agent to stop getting worse over time.
