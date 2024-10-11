from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='natural_language_terminal',
    version='0.1.7',  # Increment the version number
    packages=[
        'natural_language_terminal',
        'natural_language_terminal.cli',
        'natural_language_terminal.core',
        'natural_language_terminal.git',
        'natural_language_terminal.terminal',
    ],
    package_data={
        'natural_language_terminal': [
            'shell_scripts/*.sh',
            'shell_scripts/*.bat'
        ],
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    author='Balaji Rama',
    author_email='balajirw10@gmail.com',
    python_requires='>=3.6',
    install_requires=['openai', 'typer', 'rich', 'python-dotenv'],
    entry_points={
        "console_scripts": [
            "nlt=natural_language_terminal.cli.app:app",
        ],
    },
)