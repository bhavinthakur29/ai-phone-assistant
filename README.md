# **AXION**

[![Release](https://img.shields.io/github/v/release/bhavinthakur29/axion-engine)](https://github.com/bhavinthakur29/axion-engine/releases)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange)](https://github.com/bhavinthakur29/axion-engine)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)

A modular and extensible automation engine.

Axion provides the execution layer that allows AI systems and applications to interact with devices, operating systems, and services through a unified architecture.

---

# Vision

Axion is not an AI assistant.

It is the automation engine behind AI assistants.
```
AI Assistant
|
v
Axion
|
v
Devices & Services
```

Future AI systems, including TULSI, will use Axion as their execution layer.

---

# Features

Current:

- Modular architecture
- Centralized logging system
- Configuration management
- Runtime context management
- Android ADB communication layer


Planned:

- Android automation
- Windows automation
- Linux automation
- Browser automation
- Docker control
- Raspberry Pi support
- Home Assistant integration
- Cloud service automation
- Plugin system

---

# Architecture

Axion is designed around independent subsystems.
```
axion/

├── brain/
│ AI integration
│ NLP
│ Speech
│
├── oracle/
│ Knowledge system
│ Capabilities
│ Preferences
│
├── arsenal/
│ Executable actions
│
├── nexus/
│ Communication layer
│ ADB
│ Win32
│ Browser
│
├── devices/
│ Device abstractions
│
├── vault/
│ Configuration
│ Runtime state
│
├── chronicle/
│ Logging
│
├── sentinel/
│ Monitoring
│
├── cli/
│ User interface
│
└── workflows/
Automation workflows
```

---

# Current Status

Version:
```v0.1.0-dev```


Current milestone:

Sprint 1 — Foundation

Completed:

✅ Repository structure

✅ Chronicle

✅ Vault

✅ Nexus


Currently developing:

⬜ Android Device abstraction


---

# Installation

Axion is currently under active development.

Installation instructions will be added after the first stable release.

---

# Development

Requirements:

- Python 3.12+
- Android Debug Bridge (ADB)


Clone:

```bash
git clone https://github.com/bhavinthakur29/ai-phone-assistant

cd axion
```
Create environment:
```bash
python -m venv .venv
```
### Activate:

- Windows:
```bash
.venv\Scripts\activate
```
- Linux/macOS:
```bash
source .venv/bin/activate
```

# Development Philosophy

Axion follows these principles:
- One responsibility per subsystem
- Modular architecture
- Replaceable components
- AI-agnostic design
- Explicit dependencies
- No unnecessary coupling
- Preserve functionality during refactoring

# Documentation

Project documentation:
```
docs/

├── AXION_CONTEXT.md
├── ROADMAP.md
└── LAST_SESSION.md
```

# Contributing

Contribution guidelines will be added when Axion reaches public development stage.

# License

Not decided yet.