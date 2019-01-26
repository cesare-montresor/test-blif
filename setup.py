from setuptools import setup

import re

version = re.search(
    '^__version__ *= *"(.*)".*$',
    open('testblif/testblif.py').read(),
    re.M
).group(1)

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name = "testblif",
    packages = ['testblif'],
    entry_points = {
        'console_scripts': ['testblif = testblif.testblif:main']
    },
    version=version,
    description = "Unit-testing-style for .blif files for Berkeley SIS.",
    long_desc = long_descr,
    author = "Cesare Montresor",
    author_email = "cesare.montresor@gmail.com",
    url = "https://github.com/cesare-montresor/test-blif",
    install_requires=[
        'prettytable>=0.7.2',
        'ptable>=0.9.2'
    ]
)