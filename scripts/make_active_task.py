#!/usr/bin/env python3
import argparse
from pathlib import Path

TEMPLATE = """# Active Task

## Goal
{goal}

## Current Status
{status}

## Key Constraints
{constraints}

## Important Details
{details}

## Next Step
{next_step}
"""


def main():
    p = argparse.ArgumentParser(description='Write a compact active-task handoff file.')
    p.add_argument('--out', default='memory/active_task.md')
    p.add_argument('--goal', required=True)
    p.add_argument('--status', required=True)
    p.add_argument('--constraints', default='- None provided')
    p.add_argument('--details', default='- None provided')
    p.add_argument('--next-step', required=True)
    args = p.parse_args()

    content = TEMPLATE.format(
        goal=args.goal,
        status=args.status,
        constraints=args.constraints,
        details=args.details,
        next_step=args.next_step,
    )
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding='utf-8')
    print(out)


if __name__ == '__main__':
    main()
