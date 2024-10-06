# setup.py
from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='natural-language-terminal',
    version='0.1.0',
    packages=find_packages(),
    long_description=open('README.md').read(),
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