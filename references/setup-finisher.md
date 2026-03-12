# Setup finisher

## What problem this solves
A tool can be “installed” but still unusable because the last mile is missing.

Typical causes:
- missing env vars
- missing login or cookies
- browser dependency not installed
- MCP endpoint not registered
- permission mismatch
- doctor/check command gives a false positive

## Practical fix
Treat setup as complete only when a real end-to-end action succeeds.

Use this checklist:
1. package/CLI exists
2. required runtime dependencies exist
3. auth/login/cookies are present
4. config points to the correct endpoint
5. a real sample action works

## Good safeguard
Leave behind a known-good command or checklist so the next run starts from a working baseline.

## Why beginners care
“Installed” means “usable” in their mind. Good tooling should respect that.
