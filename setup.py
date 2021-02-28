import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='gitlinks',  
    version='0.1',
    scripts=['gitlinks'] ,
    author='Logan Engstrom',
    author_email='logan@mit.edu',
    description='GitHub pages-powered shortlinks.'
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/lengstrom/gitlinks',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console"
    ]
 )