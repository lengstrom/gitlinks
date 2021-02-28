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
import tabulate
import json
import git
import pandas as pd
from utils import clone, query_yes_no, try_setup, serialize_csv, load_csv
from utils import commit_push, check_repo, generate_pages, prettify_list, clean
from utils import patch_url

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
    url = patch_url(url)
    df = df[df.key != key]
    df = df.append(pd.Series({
        'key':key,
        'url':url
    }), ignore_index=True)

    return df

def delete_link(key, df):
    return df[df.key != key]


def show(df, repo):
    df['=>'] = ['=>' for _ in range(df.shape[0])]
    new_order = [0, 2, 1]
    df = df[df.columns[new_order]]
    df = df.sort_values('key')

    x = tabulate.tabulate(df, df.columns, colalign=('left', 'center', 'left'),
                          showindex=False)
    width = x.split('\n')[0].index('=>') - 6
    title = 'GitLinks Index'
    print(' ' * width + title)
    x = '\n'.join(x.split('\n')[2:])
    #print('-' * max(map(len, x.split('\n'))))
    print(x)
    print(f'\nGit Remote: {repo.remotes.origin.url}')

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
    
    repo.git.reset('--hard', repo.active_branch)
    clean(repo)

    print('=> Checking for changes from remote...')
    repo.remotes.origin.pull()

    if args['set']:
        key = args['<key>']
        url = args['<url>']
        df = set_link(key, url, df)
        commit_msg = f'Set key "{key}" => "{url}"'
    elif args['delete']:
        key = args['<key>']
        if ',' in key:
            keys = key.split(',')
        else:
            keys = [key]

        poss = set(df.key)
        deletable = [k for k in keys if k in poss]
        for key in deletable:
            df = delete_link(key, df)

        not_deletable = set(keys) - set(deletable)
        if not_deletable:
            keys_pretty = prettify_list(not_deletable)
            print(f'=> Key {keys_pretty} not present...')

        if len(deletable) > 0:
            keys_pretty = prettify_list(deletable)
            commit_msg = f'Removed key {keys_pretty}'
        else:
            print('=> No key to remove, exiting!')
            return

    serialize_csv(df, csv_path)
    generate_pages(df, GIT_PATH, INDEX_NAME)

    try:
        print('=> Committing and pushing...')
        commit_push(repo, commit_msg[:50])
        print(f'=> Success: {commit_msg}')
    except Exception as e:
        repo.git.reset('--hard',f'origin/{repo.active_branch}')
        print(f'=> Failed; rolling back.')
        raise e

if __name__ == '__main__':
    args = docopt(__doc__)

    with ILock('gitlinks'):
        main(args)
