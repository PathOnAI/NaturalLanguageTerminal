<p align="center">
  <img src="nls.png" width="60%" alt="NLS-logo">
</p>
<p align="center">
    <h1 align="center">Natural Language Shell</h1>
</p>
<p align="center">
	<!-- local repository, no metadata badges. --></p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI">
	<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=flat-square&logo=TypeScript&logoColor=white" alt="TypeScript">
	<img src="https://img.shields.io/badge/tsnode-3178C6.svg?style=flat-square&logo=ts-node&logoColor=white" alt="tsnode">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON">
</p>

# NLS Git AutoCommit
repo owner: Balaji Rama (balajirw10@gmail.com)

This package provides a command-line tool for automatically generating commit messages using an LLM based on git diffs.

## Installation

1. Clone this repository
2. Navigate to the project directory
3. Run `pip install .`

## Usage

1. Create a new NLS environment:
   ```
   python -m nls myenv
   ```

2. Activate the NLS environment:
   ```
   source myenv/bin/activate
   ```

3. Use git autocommit:
   ```
   git autocommit
   ```

4. Deactivate the NLS environment when you're done:
   ```
   deactivate
   ```

Make sure to set your OpenAI API key as an environment variable:
```
export OPENAI_API_KEY='your-api-key-here'
```
