import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='gitlinks',  
    version='0.2',
    author='Logan Engstrom',
    author_email='logan@mit.edu',
    description='GitHub pages-powered shortlinks.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/lengstrom/gitlinks',
    packages=setuptools.find_packages(),
    install_requires=[
        'docopt>=0.6.2',
        'GitPython>=3.1.13',
        'ilock>=1.0.3',
        'pandas>=1.2.2',
        'portalocker>=2.2.1',
        'requests>=2.25.1',
        'requests-toolbelt>=0.9.1',
        'tabulate>=0.8.9',
        'tqdm>=4.58.0'
    ],
    entry_points={
        'console_scripts':[
            'gitlinks=gitlinks.cli:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console"
    ],
    python_requires=">=3.6"
 )