#!/usr/bin/env python
# -*- coding: utf-8 -*-
# stolen from imgcat: https://github.com/wookayin/python-imgcat/blob/master/setup.py

import sys
import os
import re
from setuptools import setup, Command

with open("README.md", "r") as fh:
    long_description = fh.read()

# setuptools.setup(
#     name='gitlinks',
#     version='0.2',
#     author='Logan Engstrom',
#     author_email='logan@mit.edu',
#     description='GitHub pages-powered shortlinks.',
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url='https://github.com/lengstrom/gitlinks',
#     packages=setuptools.find_packages(),
#     install_requires=[
#     ],
#     entry_points={
#         'console_scripts':['gitlinks=gitlinks.cli:main']
#     },
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
#         "Operating System :: OS Independent",
#         "Development Status :: 4 - Beta",
#         "Environment :: Console"
#     ],
#  )

__PATH__ = os.path.abspath(os.path.dirname(__file__))

def read_readme():
    with open('README.md') as f:
        return f.read()

def read_version():
    # importing the package causes an ImportError :-)
    with open(os.path.join(__PATH__, 'imgcat/__init__.py')) as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  f.read(), re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find __version__ string")


install_requires = [
    'docopt>=0.6.2',
    'GitPython>=3.1.13',
    'ilock>=1.0.3',
    'pandas>=1.2.2',
    'portalocker>=2.2.1',
    'requests>=2.25.1',
    'requests-toolbelt>=0.9.1',
    'tabulate>=0.8.9',
    'tqdm>=4.58.0',
    'twine'
]

tests_requires = [
    'pytest<5.0'
]

__version__ = read_version()


# brought from https://github.com/kennethreitz/setup.py
class DeployCommand(Command):
    description = 'Build and deploy the package to PyPI.'
    user_options = []

    def initialize_options(self): pass
    def finalize_options(self): pass

    @staticmethod
    def status(s):
        print(s)

    def run(self):
        import twine  # we require twine locally

        assert 'dev' not in __version__, \
            "Only non-devel versions are allowed. __version__ == {}".format(__version__)

        with os.popen("git status --short") as fp:
            git_status = fp.read().strip()
            if git_status:
                print("Error: git repository is not clean.\n")
                os.system("git status --short")
                sys.exit(1)

        try:
            from shutil import rmtree
            self.status('Removing previous builds ...')
            rmtree(os.path.join(__PATH__, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution ...')
        os.system('{0} setup.py sdist'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine ...')
        os.system('twine upload dist/*')

        self.status('Creating git tags ...')
        os.system('git tag v{0}'.format(__version__))
        os.system('git tag --list')
        sys.exit()

setup(
    name='gitlinks',
    version=__version__,
    license='MIT',
    description='GitHub pages-powered golinks',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/lengstrom/gitlinks',,
    author='Logan Engstrom',
    author_email='engstrom@mit.com',
    keywords='golinks github pages',
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    packages=['imgcat'],
    install_requires=install_requires,
    setup_requires=['pytest-runner<5.0'],
    tests_require=tests_requires,
    entry_points={
        'console_scripts': ['gitlinks=gitlinks:main'],
    },
    include_package_data=True,
    zip_safe=False,
    cmdclass={
        'deploy': DeployCommand,
    }
    python_requires=">=3.6")