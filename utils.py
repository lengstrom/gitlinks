import git
from collections import defaultdict
from git import RemoteProgress
import pandas as pd
import shutil
import sys
from pathlib import Path

def empty_csv():
    return pd.DataFrame({
        'key':[],
        'url':[]
    })

def serialize_csv(df, path):
    df.to_csv(str(path), index=False)

def load_csv(f):
    return pd.read_csv(str(f))

class CloneProgress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        if message:
            print(message)

def clone(url, path):
    prog = CloneProgress()
    return git.Repo.clone_from(url, path, progress=prog)

def commit_push(repo, commit_msg):
    repo.git.add(all=True)
    repo.index.commit(commit_msg)
    origin = repo.remote(name='origin')
    origin.push()

def clean(repo):
    repo.git.clean('-xdf')

def check_repo(repo, index_name):
    wd = repo.working_dir
    try:
        load_csv(str(Path(wd) / index_name))
        return True
    except:
        return False

def wipe_directory(dired, protected):
    protected = set(protected)
    for child in dired.iterdir():
        if child.name not in protected:
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()

def try_setup(repo, path, index_name):
    # path is the path of a git repository
    # Clean up any non-tracked changes
    # Then check if there's an index.csv; if so, exit
    # If no index.csv, delete everything in repo, make an empty index.csv
    clean(repo)
    index_path = path / index_name

    if not check_repo(repo, index_name):
        print('Index not found; initializing index!')
        # delete everything in directory
        wipe_directory(path, ['.git'])

        empty = empty_csv()
        serialize_csv(empty, index_path)
        try:
            commit_push(repo, 'Initialization')
        except Exception as e:
            print('Remote update failed; try initializing again!')
            raise e

def template_maker(url):
    return f'<meta http-equiv="refresh" content="0; URL={url}"/>'

def generate_pages(df, working_dir, index_name):
    wd = Path(working_dir)
    protected = ['.git', index_name]
    wipe_directory(wd, protected)

    parent_cache = defaultdict(list)
    for _, row in df.iterrows():
        key, url = row.key, row.url
        html_file = wd / (key + '.html')
        parent = html_file.parent
        if not parent in parent_cache:
            parent.mkdir(exist_ok=True, parents=True)

        parent_cache[parent].append((key.split('/')[-1], url, 'key'))

        with open(html_file, 'w+') as f:
            f.write(template_maker(url))

    for parent, _ in list(parent_cache.items()):
        while parent != wd:
            parent_cache[parent.parent] = (parent.name, parent.name, 'dired')
            parent = parent.parent

    for parent, ls in parent_cache.items():
        out_filepath = parent / 'index.html'

        ls = sorted(ls, key=lambda x:x[0])
        print(ls)
        direds = [k for k in ls if k[2] == 'dired']
        keys = [k for k in ls if k[2] != 'dired']

        strs = add_links(direds, 'Directories', is_dired=True)
        keys = add_links(keys, 'Links', is_dired=False)

        html = ''.join(strs + keys)
        with open(out_filepath, 'w+') as f:
            f.write(html)

def add_links(keys, header, is_dired=False):
    strs = [f'<h3>{header}</h3><br><ul>']
    for name, url, _ in keys:
        if not is_dired:
            item = f'<li><a href="{url}">{name}</a> &#x2192; <a href="{url}">{url}</a></li>'
        else:
            item = f'<li><a href="{url}/">{name}/</a></li>'
        strs.append(item)
    strs.append('</ul>')
    return strs
 
# This is from StackOverflow.
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")