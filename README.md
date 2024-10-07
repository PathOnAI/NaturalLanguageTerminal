# Natural Language Terminal (NLT)

<p align="center">
  <img src="https://github.com/PathOnAI/NaturalLanguageTerminal/blob/main/nlt.png" width="60%" alt="nlt-logo">
</p>

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

## 🌟 Overview

NLT is a groundbreaking tool that allows you to interact with your terminal using natural language. Say goodbye to complex command syntaxes and hello to intuitive, conversational computing.

## 🚀 Features

- **🗣️ Intuitive Commands**: Interact with your terminal using natural language
- **🧠 Smart Environment Management**: Create and manage virtual environments effortlessly
- **🌐 Cross-Platform**: Seamless operation on macOS and Windows
- **🪶 Lightweight**: Minimal overhead, maximum performance

## 📦 Installation

```bash
python -m pip install natural-language-terminal
```

### macOS

```bash
@nlt init
```

### Windows

```powershell
nlt init
```

## 🔮 Usage

### Creating a New Environment

#### macOS

```bash
@nlt create my_awesome_project
```

#### Windows

```powershell
nlt create my_awesome_project
```

### Activating an Environment

#### macOS

```bash
source my_awesome_project/bin/activate
```

#### Windows

```powershell
cd my_awesome_project/Scripts
activate.bat
```

### Deactivating and Cleaning Up

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

## 🛠️ How It Works

NLT uses natural language processing to interpret your commands and translate them into powerful terminal operations. This abstraction layer allows you to focus on your intentions rather than syntax.

## 🔌 Plugins

NLT supports plugins to extend its functionality with additional commands. These plugins are provided by different providers, enhancing your NLT experience with specialized features.

### Available Providers

Currently, NLT supports the following plugin provider:

#### Git Provider

The Git provider adds Git-related functionality to your NLT session.

Available commands:

- `git autocommit`: Automatically generates a commit message and commits changes.

Usage:
```bash
git autocommit
```

This command analyzes your changes, generates an appropriate commit message, and creates a new commit.

## 🤝 Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get started.

## 📜 License

nlt is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🔮 Future Plans

- 🖥️ Enhanced Windows support
- 🧠 Advanced AI-driven command predictions
- 🔗 Integration with popular development tools and frameworks
- 🌐 Multi-language support

## 🙏 Acknowledgments

A big thank you to all our contributors and supporters who help make NLT better every day.

---

<p align="center">
  <em>"Speak to your terminal, and it shall listen."</em>
</p>


