"""GitLinks: Command line client for managing GitHub pages-powered shortlinks.
See https://github.com/lengstrom/gitlinks#setup for setup and additional usage
information.

Usage:
  gitlinks init <git remote>
  gitlinks set <key> <url>
  gitlinks delete <key> ...
  gitlinks show

Options:
  -h --help     Show this screen.
"""
from docopt import docopt
from pathlib import Path
import shutil
import tabulate
import json
import git
import pandas as pd
import sys
from ilock import ILock

from .utils import (
    clone, query_yes_no, try_setup, serialize_csv, load_csv, commit_push,
    check_repo, generate_pages, plural_msg, clean, patch_url, reset_origin,
    ARROW
)

GIT_PATH = Path('~/.gitlinks/').expanduser()
INDEX_NAME = 'index.csv'

def initialize(url, path=GIT_PATH):
    if path.exists():
        msg = f'{path} already exists; really delete?'
        if query_yes_no(msg, default='yes'):
            shutil.rmtree(path)
        else:
            print('Ok, exiting.')
            return

    repo = clone(url, path)
    try_setup(repo, path, INDEX_NAME)
    print(f'Initialized gitlinks to url: {url}!')

def set_link(key, url, df):
    url = patch_url(url)
    df = df[df.key != key]
    df = df.append(pd.Series({
        'key':key,
        'url':url
    }), ignore_index=True)

    return df

def delete_links(keys, df):
    keys = set(keys)
    return df[~df.key.isin(keys)]

def show(df, repo):
    df[ARROW] = [ARROW for _ in range(df.shape[0])]
    new_order = [0, 2, 1]
    df = df[df.columns[new_order]]
    df = df.sort_values('key')

    title = f'== GitLinks (Remote: {repo.remotes.origin.url}) =='
    print(title)
    if df.shape[0] > 0:
        tab = tabulate.tabulate(df, df.columns, colalign=('left', 'center', 'left'),
                                showindex=False)
        # width = tab.split('\n')[0].index(ARROW) - len(title)//2
        # width = min(0, width)
        # print(' ' * width + title)
        rows = '\n'.join(tab.split('\n')[2:])
        print(rows)
    else:
        print('=> Empty, no keys to display!')

def execute(args, git_path=GIT_PATH):
    if args['init']:
        return initialize(args['<git remote>'], path=git_path)

    repo = git.Repo(git_path)
    if not check_repo(repo, INDEX_NAME):
        msg = "No initialized repo; run `gitlinks init <url>` first!"
        raise ValueError(msg)

    csv_path = git_path / INDEX_NAME
    df = load_csv(csv_path)

    reset_origin(repo)
    clean(repo)
    print('=> Checking for changes from remote...')
    repo.remotes.origin.pull()

    if args['show']:
        return show(df, repo)

    if args['set']:
        key = args['<key>'][0]
        assert key[-1] != '/', f'Key "{key}" should not end with a "/"!'
        url = args['<url>']
        df = set_link(key, url, df)
        commit_msg = f'Set key "{key}" {ARROW} "{url}"'
    elif args['delete']:
        keys = args['<key>']
        poss = set(df.key)
        deletable = [k for k in keys if k in poss]
        df = delete_links(deletable, df)

        not_deletable = set(keys) - set(deletable)
        if not_deletable:
            msg = '=> Key{plural} {keys_pretty} not present...'
            print(plural_msg(not_deletable, msg))

        commit_msg = plural_msg(deletable, '=> Deleted key{plural} {keys_pretty}')
        if len(deletable) == 0:
            print('=> No keys to remove, exiting!')
            return

    serialize_csv(df, csv_path)
    generate_pages(df, git_path, INDEX_NAME)

    try:
        print('=> Committing and pushing...')
        commit_push(repo, commit_msg[:50])
        print(f'=> Success: {commit_msg}.')
    except Exception as e:
        reset_origin(repo)
        print(f'=> Failed; rolling back.')
        raise e

def main():
    if len(sys.argv) == 1:
        sys.argv.append('-h')

    args = docopt(__doc__)
    with ILock('gitlinks'):
        execute(args)

if __name__ == '__main__':
    main()
