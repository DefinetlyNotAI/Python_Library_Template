# Guide to Upload PyPI libraries

Use the 2 python files attached and modify for your needs,

Opne cmd inside the directory of the library

`python setup.py sdist bdist_wheel`
`twine upload dist/* --verbose`

Use the API key from your PyPI account.

(Do note you need to install twine via `pip install twine`)
