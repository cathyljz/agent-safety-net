#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

KEEP_DEFAULT = ['id', 'name', 'title', 'status', 'state', 'url', 'error', 'message']


def trim(obj, keep):
    if isinstance(obj, dict):
        return {k: trim(v, keep) for k, v in obj.items() if k in keep}
    if isinstance(obj, list):
        return [trim(x, keep) for x in obj[:20]]
    return obj


def main():
    p = argparse.ArgumentParser(description='Reduce large JSON/tool payloads.')
    p.add_argument('input')
    p.add_argument('--keep', nargs='*', default=KEEP_DEFAULT)
    args = p.parse_args()

    data = json.loads(Path(args.input).read_text(encoding='utf-8'))
    reduced = trim(data, set(args.keep))
    print(json.dumps(reduced, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
