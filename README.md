# AXION

> **Execution Engine for AI Systems**

[![Release](https://img.shields.io/github/v/release/bhavinthakur29/axion-engine)](https://github.com/bhavinthakur29/axion-engine/releases)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange)](https://github.com/bhavinthakur29/axion-engine)
[![License](https://img.shields.io/github/license/bhavinthakur29/axion-engine)](LICENSE)

Axion is a modular, extensible automation engine that enables AI assistants and applications to interact with devices, operating systems, and services through a unified architecture.

---

# Vision

Axion is **not** an AI assistant.

It is the execution engine that powers AI assistants.

```text
AI Assistant
      │
      ▼
    Axion
      │
      ▼
Devices • Operating Systems • Services
```

Axion is designed to be AI-agnostic and reusable by any application that requires automation capabilities.

One planned application is **TULSI**, a portable personal AI that will use Axion as its execution engine.

---

# Project Ecosystem

```text
TekSquad

Current

└── Axion
    Automation Engine

Planned

└── TULSI
    Portable Personal AI
        │
        ▼
      Axion
```

---

# Features

## Current

- Modular subsystem architecture
- Centralized logging (Chronicle)
- Configuration management (Vault)
- Runtime context management
- Android ADB communication layer (Nexus)

## Planned

- Android automation
- Windows automation
- Linux automation
- Browser automation
- Docker automation
- Raspberry Pi support
- Home Assistant integration
- Cloud service automation
- REST API integrations
- Plugin ecosystem
- Workflow engine

---

# Architecture

Axion is composed of independent, replaceable subsystems.

```text
axion/

├── brain/
│   AI integration
│   NLP
│   Speech
│
├── oracle/
│   Knowledge
│   Device capabilities
│   User preferences
│
├── arsenal/
│   Executable actions
│
├── nexus/
│   Communication layer
│   ADB
│   Win32
│   Browser
│
├── devices/
│   Device abstractions
│
├── vault/
│   Configuration
│   Runtime state
│
├── chronicle/
│   Logging
│
├── sentinel/
│   Monitoring
│
├── cli/
│   Command-line interface
│
└── workflows/
    Automation workflows
```

---

# Current Status

**Version**

```text
v0.1.0-dev
```

**Sprint 1 — Foundation**

Completed

- ✅ Repository Architecture
- ✅ Chronicle
- ✅ Vault
- ✅ Runtime Context
- ✅ Nexus

In Progress

- ⬜ Android Device Abstraction

---

# Installation

Axion is currently under active development.

Installation instructions will be provided with the first stable release.

---

# Development

## Requirements

- Python 3.12+
- Android Debug Bridge (ADB)

Clone the repository:

```bash
git clone https://github.com/bhavinthakur29/axion-engine.git

cd axion-engine
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Development Philosophy

Axion follows a modular architecture based on a few core principles.

- One responsibility per subsystem
- Explicit dependency boundaries
- AI-agnostic design
- Composition over inheritance
- Replaceable components
- Production-ready code
- Preserve functionality while refactoring

---

# Documentation

Project documentation is available in:

```text
docs/

├── AXION_CONTEXT.md
├── ROADMAP.md
└── LAST_SESSION.md
```

---

# Roadmap

Current milestone:

**Sprint 1 — Foundation**

Upcoming milestones include:

- Android Device abstraction
- Command Line Interface
- Action Registry
- Executor
- Arsenal
- Brain
- Oracle
- Workflow Engine
- Windows support
- Browser automation
- Plugin system
- TULSI integration

A detailed roadmap is available in:

```text
docs/ROADMAP.md
```

---

# Contributing

Contributing guidelines will be published once Axion reaches its first public development milestone.

---

# License

Licensed under the Apache License, Version 2.0.

See the [LICENSE](LICENSE) file for details.