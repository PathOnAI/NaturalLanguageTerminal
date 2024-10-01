from setuptools import setup, find_packages

setup(
    name="nls",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "typer[all]",
        "rich",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "@nls=nls.cli.app:app",
        ],
    },
    package_data={
        'nls': [
            'shell_scripts/*.sh',
            'shell_scripts/*.bat'
        ],
    },
)