# setup.py
from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

# Read the contents of requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='natural-language-terminal',
    version='{{VERSION_PLACEHOLDER}}',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    author='Balaji Rama',
    author_email='balajirw10@gmail.com',
    python_requires='>=3.6',
    install_requires=required,
    entry_points={
        "console_scripts": [
            "@nlt=nlt.cli.app:app",
        ],
    },
    package_data={
        'pynlt': [
            'shell_scripts/*.sh',
            'shell_scripts/*.bat'
        ],
    },
)