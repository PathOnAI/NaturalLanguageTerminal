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