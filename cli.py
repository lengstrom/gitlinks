"""GitLinks: GitHub pages-powered shortlinks. See: https://github.com/lengstrom/gitlinks.

Usage:
  gitlinks init <url>
  gitlinks set <key> <url>
  gitlinks delete <key>
  gitlinks show

Options:
  -h --help     Show this screen.
  -v --version  Show version.
"""
from ilock import ILock
from docopt import docopt
from pathlib import Path
import shutil
import json
import git
import pandas as pd
from utils import clone, query_yes_no, try_setup, serialize_csv, load_csv
from utils import commit_push, check_repo, generate_pages

GIT_PATH = Path('~/.gitlinks/').expanduser()
INDEX_NAME = 'index.csv'

def initialize(url, path=GIT_PATH):
    if path.exists():
        if query_yes_no(f'{path} already exists; really delete?', default='yes'):
            shutil.rmtree(path)
        else:
            print('Ok, exiting...')
            sys.exit()

    repo = clone(url, path)
    try_setup(repo, path, INDEX_NAME)
    print(f'Successfully initialized gitlinks to url: {url}')

def set_link(key, url, df):
    df = df[df.key != key]
    df = df.append(pd.Series({
        'key':key,
        'url':url
    }), ignore_index=True)

    return df

def delete_link(key, df):
    return df[df.key != key]

def show(df, repo):
    df['->'] = ['->' for _ in range(df.shape[0])]

    new_order = [0, 2, 1]
    df = df[df.columns[new_order]]
    df = df.rename(lambda x:x.upper(), axis=1)
    df = df.sort_values('KEY')
    print(df.to_string(index=False)) #, justify=['right', 'center', 'left']))
    print('')
    print(f'Git Remote: {repo.remotes.origin.url}')

def main(args):
    if args['init']:
        return initialize(args['<url>'])

    repo = git.Repo(GIT_PATH)
    if not check_repo(repo, INDEX_NAME):
        msg = "No initialized repo; run `gitlinks init <url>` first!"
        raise ValueError(msg)

    csv_path = GIT_PATH / INDEX_NAME
    df = load_csv(csv_path)

    if args['show']:
        return show(df, repo)

    if args['set']:
        key = args['<key>']
        url = args['<url>']
        df = set_link(key, url, df)
        commit_msg = f'Set {key} -> {url}'
    elif args['delete']:
        key = args['<key>']
        df = delete_link(key, df)
        commit_msg = f'Removed {key}'

    serialize_csv(df, csv_path)
    generate_pages(df, GIT_PATH, INDEX_NAME)

    try:
        commit_push(repo, commit_msg[:50])
        print(f'Success: {commit_msg}')
    except Exception as e:
        repo.git.reset('--hard','origin/master')
        print(f'Failed; rolling back')
        raise e

if __name__ == '__main__':
    args = docopt(__doc__)

    with ILock('gitlinks'):
        main(args)
