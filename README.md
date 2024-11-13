# Natural Language Terminal (NLT)
repo owner: Balaji Rama (balajirw10@gmail.com)

<p align="center">
  <strong>Welcome to the future of command-line interfaces.</strong>
</p>

<p align="center">
  Natural Language Terminal (NLT) revolutionizes the way you interact with your system, bringing the power of natural language processing to your fingertips.
</p>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-plugins">Plugins</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-license">License</a>
</p>

---

<h2>Note: Windows compatibility is still under development, so instructions & usage are unstable</h2>

## 🌟 1. Overview

NLT is a groundbreaking tool that allows you to interact with your terminal using natural language. Say goodbye to complex command syntaxes and hello to intuitive, conversational computing.

## 🚀 2. Features

- **🗣️ Intuitive Commands**: Interact with your terminal using natural language
- **🧠 Smart Environment Management**: Create and manage virtual environments effortlessly
- **🌐 Cross-Platform**: Seamless operation on macOS and Windows
- **🪶 Lightweight**: Minimal overhead, maximum performance

## 📦 3. Get Started
### 3.1 prerequisite
Install Xcode from the Mac App Store:

Open the Mac App Store
Search for "Xcode"
Click "Get" or "Install"
The download might take a while as Xcode is a large application (several GB)


Once Xcode is fully installed, then try running the command again:
```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

### 3.2 Installation
This project is developed using Python 3.10. Follow these steps to set up your environment on Mac:
1. Install Python 3.10 using Homebrew:
```bash
brew install python@3.10
```

2. Link Python 3.10:
```bash
brew link python@3.10
```

3. Add Python aliases to your shell configuration:
```bash
echo 'alias python="/opt/homebrew/bin/python3.10"' >> ~/.zshrc
echo 'alias python3="/opt/homebrew/bin/python3.10"' >> ~/.zshrc
```

4. Apply the changes:
```bash
source ~/.zshrc
```

5. Verify your Python installation:
```bash
python --version  # Should show Python 3.10.x
python3 --version  # Should show Python 3.10.x
```
#### Installing Project Dependencies

1. Install the natural-language-terminal package:
```bash
python -m pip install natural-language-terminal
```

2. Install required system utilities:
```bash
python -m pip install psutil
```

#### Troubleshooting

If you encounter any module-related errors, try reinstalling the packages:
```bash
python -m pip uninstall natural-language-terminal
python -m pip install natural-language-terminal psutil
```

#### NL session initialization
```bash
nlt init
```

### 3.3 Usage

#### Creating a New Environment


```bash
nlt create my_awesome_project
```


#### Activating an Environment


```bash
source my_awesome_project/bin/activate
```


#### Deactivating and Cleaning Up

For both macOS and Windows:

```bash
remove
```

To remove the environment and clean up:

```bash
remove -c
```

or

<!-- ```bash
remove --clean
``` -->


## 🤝 4. Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get started.

[![NaturalLanguageTerminal contributors](https://contrib.rocks/image?repo=PathOnAI/NaturalLanguageTerminal)](https://github.com/PathOnAI/NaturalLanguageTerminal/graphs/contributors)


---

<p align="center">
  <em>"Speak to your terminal, and it shall listen."</em>
</p>


