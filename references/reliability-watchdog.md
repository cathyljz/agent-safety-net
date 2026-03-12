# Reliability watchdog

## What problem this solves
Agents often look broken when they are actually:
- waiting for approval
- blocked on a hidden question
- stuck retrying a tool
- hung on a long command
- half-failed after partial output

## Practical fix
Before assuming the agent is dead:
1. check whether it is waiting on permission or user input
2. check whether a background task is still running
3. check the last successful step
4. show the blocker in plain language
5. offer the shortest recovery action

## Good safeguard
Always prefer status that says:
- current step
- blocker
- next action

instead of dumping raw logs.

## Why beginners care
Beginners describe this as “it froze”. A good watchdog turns that into something understandable and fixable.
