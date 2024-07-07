# Guide to Upload PyPI libraries

## Setup
Use the 2 python files attached and modify for your needs,

For `__init__.py`, Replace `LIBRARY_NAME` from the line's `from.LIBRARY_NAME import *` for any extra files you have that include classes, so if I have a file called `Algorithims.py`, I add the following line: `from.Algorithims import *`.

For `setup.py`, Replace anything with `CHANGE_ME` in it, This includes name, version, description, author, author email, classifiers and anything with comments, The higher quality the `setup.py` file is, the better your library becomes.

## Launch
After everything, Open cmd inside the directory of the library

`python setup.py sdist bdist_wheel`

`twine upload dist/* --verbose`

Use the API key from your PyPI account if asked.

(Do note you need to install twine via `pip install twine`)
