#!/usr/bin/env python3
"""Read-only reference: validate work records, select work, render a packet.

No executor, claims, scheduling, transitions, or approval inference.
"""
import argparse
import json
from pathlib import Path
import sys

STATES = {'ready', 'active', 'submitted', 'accepted', 'blocked', 'deferred', 'stopped'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def local_file(root, name):
    require(text(name), 'artifact path must be non-empty text')
    path = (root / name).resolve()
    require(not Path(name).is_absolute() and path.is_relative_to(root),
            'artifact must stay inside the ledger directory')
    require(path.is_file() and path.stat().st_size > 0, f'missing/empty artifact: {name}')
    return path


def validate(data, root):
    """Reject malformed state instead of treating it as an empty or ready queue."""
    require(isinstance(data, dict) and type(data.get('version')) is int and data['version'] == 1, 'expected version 1')
    streams = data.get('workstreams')
    tasks = data.get('tasks')
    require(isinstance(streams, dict) and streams, 'workstreams must be a non-empty object')
    for key, stream in streams.items():
        require(text(key) and isinstance(stream, dict) and text(stream.get('outcome')),
                'each workstream needs an ID and outcome')
    require(isinstance(tasks, list), 'tasks must be an array')
    by_id = {}
    for task in tasks:
        require(isinstance(task, dict), 'task must be an object')
        tid = task.get('id')
        require(text(tid) and tid not in by_id, 'task IDs must be non-empty and unique')
        by_id[tid] = task
        require(text(task.get('workstream')) and task['workstream'] in streams,
                f'{tid}: unknown workstream')
        for field in ('title', 'acceptance'):
            require(text(task.get(field)), f'{tid}: missing {field}')
        require(isinstance(task.get('state'), str) and task['state'] in STATES,
                f'{tid}: unknown state')
        require(type(task.get('priority')) is int and task['priority'] > 0,
                f'{tid}: priority must be a positive integer')
        deps = task.get('depends_on')
        require(isinstance(deps, list) and all(text(d) for d in deps)
                and len(deps) == len(set(deps)), f'{tid}: invalid dependencies')
        if task['state'] in {'blocked', 'deferred'}:
            require(text(task.get('wake')), f'{tid}: missing observable wake condition')
        if task['state'] in {'submitted', 'accepted'}:
            result = task.get('result')
            require(isinstance(result, dict), f'{tid}: missing result')
            for field in ('attempt', 'artifact_version', 'finding', 'residual'):
                require(text(result.get(field)), f'{tid}: result needs {field}')
            local_file(root, result.get('contract'))
            local_file(root, result.get('evidence'))
        if task['state'] in {'accepted', 'stopped'}:
            decision = task.get('decision')
            require(isinstance(decision, dict), f'{tid}: missing decision')
            for field in ('by', 'authority', 'reason'):
                require(text(decision.get(field)), f'{tid}: decision needs {field}')
            if task['state'] == 'accepted':
                require(decision.get('artifact_version') == task['result']['artifact_version'],
                        f'{tid}: decision applies to a different artifact version')
    for tid, task in by_id.items():
        require(all(d in by_id for d in task['depends_on']), f'{tid}: unknown dependency')
    visited, visiting = set(), set()

    def visit(tid):
        require(tid not in visiting, f'dependency cycle at {tid}')
        if tid in visited:
            return
        visiting.add(tid)
        for dep in by_id[tid]['depends_on']:
            visit(dep)
        visiting.remove(tid)
        visited.add(tid)

    for tid in by_id:
        visit(tid)
    return data


def select(data):
    """Demo policy: acceptance-gated dependencies and serial active work."""
    if any(t['state'] == 'active' for t in data['tasks']):
        raise ValueError('reconcile active work before selecting another task')
    accepted = {t['id'] for t in data['tasks'] if t['state'] == 'accepted'}
    eligible = [t for t in data['tasks'] if t['state'] == 'ready'
                and set(t['depends_on']) <= accepted]
    return min(eligible, key=lambda t: (t['priority'], t['id'])) if eligible else None


def packet(data):
    lines = ['# Disposition packet', '', 'Generated view; no decisions are made by this command.', '']
    for sid, stream in data['workstreams'].items():
        lines += [f'## {sid}: {stream["outcome"]}', '']
        for task in (t for t in data['tasks'] if t['workstream'] == sid):
            lines += [f'- {task["id"]}: {task["title"]} — {task["state"]}']
            if task['state'] in {'submitted', 'accepted'}:
                result = task['result']
                lines += [f'  - Contract: {result["contract"]}',
                          f'  - Attempt: {result["attempt"]}; version: {result["artifact_version"]}',
                          f'  - Evidence: {result["evidence"]}',
                          f'  - Finding: {result["finding"]}',
                          f'  - Residual: {result["residual"]}']
                if task['state'] == 'accepted':
                    decision = task['decision']
                    lines += [f'  - Accepted by: {decision["by"]}; authority: {decision["authority"]}',
                              f'  - Decision reason: {decision["reason"]}',
                              '  - Finding delivery/acknowledgment: not tracked by this example.']
            if task['state'] in {'blocked', 'deferred'}:
                lines += [f'  - Wake: {task["wake"]}']
        lines += ['']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['check', 'next', 'packet'])
    parser.add_argument('ledger', type=Path)
    args = parser.parse_args()
    try:
        source = args.ledger.resolve()
        data = validate(json.loads(source.read_text()), source.parent)
        if args.command == 'packet':
            print(packet(data))
        elif args.command == 'next':
            task = select(data)
            print(json.dumps({'task': task, 'note': 'Selection only; no claim or execution.'}))
        else:
            print(json.dumps({'ok': True, 'tasks': len(data['tasks'])}))
    except (ValueError, OSError, RecursionError) as exc:
        print(json.dumps({'ok': False, 'error': str(exc)}), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
