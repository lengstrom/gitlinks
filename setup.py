import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='gitlinks',  
    version='0.1',
    author='Logan Engstrom',
    author_email='logan@mit.edu',
    description='GitHub pages-powered shortlinks.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/lengstrom/gitlinks',
    packages=setuptools.find_packages(),
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