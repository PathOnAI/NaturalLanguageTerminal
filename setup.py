# setup.py
from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='nlt',
    version='0.2.0',
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    author='Balaji Rama',
    author_email='balajirw10@gmail.com',
    python_requires='>=3.6',
    install_requires=required,
)