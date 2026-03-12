# Tool output reduction

## What problem this solves
Many tools return giant JSON blobs, repeated metadata, or logs that are much longer than what the model actually needs.

This causes:
- token waste
- slower reasoning
- polluted context
- lower quality decisions

## Practical fix
Reduce tool output before feeding it back to the model:
- keep only required fields
- collapse repeated objects
- summarize counts, errors, and next-action fields
- extract first, reason second

## Good safeguard
Use scripts or deterministic transforms for repetitive reduction work.
Do not repeatedly paste raw tool payloads into the main context.

## Why beginners care
Users experience this as “the agent is expensive and weirdly verbose”.
