"""Prepare the exact source-only experimental checkout; no game downloads."""
import argparse
import json
from pathlib import Path
import subprocess


def run(*args, cwd=None):
    return subprocess.check_output(args, cwd=cwd, text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    spec = json.loads((root / 'upstream.json').read_text(encoding='utf-8'))
    target = args.destination.resolve()
    if target.exists():
        parser.error('destination must not exist; existing checkouts are never reset')
    run('git', 'clone', '--no-checkout', spec['repository'], str(target))
    run('git', 'checkout', '--detach', spec['commit'], cwd=target)
    if run('git', 'rev-parse', 'HEAD', cwd=target) != spec['commit']:
        raise RuntimeError('source revision mismatch')
    patch = str(root / 'current-experimental.patch')
    run('git', 'apply', '--check', patch, cwd=target)
    run('git', 'apply', patch, cwd=target)
    run('git', 'diff', '--check', cwd=target)
    print('Prepared experimental host source:', target)
    print('No game assets fetched; gameplay/GPU validation remains required.')


if __name__ == '__main__':
    main()
