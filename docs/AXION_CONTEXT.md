# AXION CONTEXT
> This file is the single source of truth for continuing development of Axion in any future ChatGPT conversation.

---

# Project

Name: Axion

Organization: TekSquad

Status: Active Development

Current Version: v0.1.0-dev

Primary Language: Python 3.12+

---

# Vision

Axion is a modular, extensible automation engine.

It is NOT just an Android automation tool.

The long-term goal is to automate:

- Android
- Windows
- Linux
- Browsers
- Raspberry Pi
- Docker
- Home Assistant
- APIs
- Cloud Services

Axion is designed to be AI-agnostic.

Future AI assistants (including TULSI) will use Axion as their execution engine.

---

# Product Ecosystem

TekSquad

├── TULSI
│   Portable Personal AI (future)
│
└── Axion
    Automation Engine

Relationship:

TULSI
    ↓
Brain
    ↓
Axion
    ↓
Devices & Services

---

# Architecture Philosophy

Every subsystem has ONE responsibility.

Never mix responsibilities.

Avoid "god classes."

Everything should be modular.

Every component should be replaceable.

---

# Current Repository Structure

axion/

brain/
core/
nexus/
devices/
arsenal/
oracle/
vault/
chronicle/
sentinel/
cli/
config/
workflows/

docs/
plugins/
tests/

---

# Core Components

## Brain

Purpose:

- Intent understanding
- NLP
- Speech
- AI integration

Never:

- Execute actions
- Talk to ADB

---

## Oracle

Purpose:

Knowledge.

Examples:

- Package names
- Installed apps
- Aliases
- Device capabilities
- User preferences

---

## Arsenal

Purpose:

Collection of executable Actions.

Examples:

OpenApp

CloseApp

Tap

Swipe

Screenshot

Media

YouTube

etc.

---

## Nexus

Purpose:

Communication layer.

Examples:

ADB

Future:

Win32

Linux

Browser

Docker

Never:

Contain business logic.

---

## Devices

Purpose:

High-level device abstraction.

Example:

AndroidDevice

Methods:

connect()

disconnect()

tap()

swipe()

launch_app()

home()

back()

etc.

---

## Vault

Purpose:

Configuration

Environment

Runtime Context

Shared Settings

---

## Chronicle

Purpose:

Centralized logging.

Every module uses Chronicle.

Never use print().

---

## Sentinel

Purpose:

Monitoring

Health checks

Failures

Watchdog

---

## CLI

Purpose:

Human interface.

CLI contains NO business logic.

CLI only:

Parse arguments

Call Engine

---

# Coding Standards

- Python 3.12+
- Type hints everywhere
- Docstrings on every public class/function
- Pathlib instead of os.path where possible
- No wildcard imports
- No print() in production
- Use Chronicle logging
- Explicit exceptions
- One responsibility per file
- Avoid circular imports
- Prefer composition over inheritance

---

# Import Style

Good

from axion.chronicle import get_logger

from axion.vault import settings

Avoid

from axion.chronicle.chronicle import ...

---

# Logging

Only Chronicle handles logging.

Example

logger.info(...)

logger.warning(...)

logger.error(...)

Never use print().

---

# Naming Philosophy

Products

Axion

TULSI

Subsystems

Brain

Oracle

Arsenal

Nexus

Chronicle

Vault

Sentinel

Actions

Verb based

OpenAppAction

CloseAppAction

TapAction

SwipeAction

Models

Object based

Device

Workflow

ActionRequest

AppAlias

---

# Dependency Rules

Allowed

Brain -> Oracle

Brain -> Vault

Executor -> Nexus

Executor -> Arsenal

Not Allowed

Nexus -> Brain

Chronicle -> Brain

Oracle -> CLI

CLI -> Nexus

---

# Current Migration Status

Repository structure:
✅ Complete

Copied modules:
✅ assistant/config.py
✅ assistant/dispatcher.py
✅ assistant/llm.py
✅ assistant/parser.py
✅ assistant/speech.py

✅ android/adb.py
✅ android/apps.py
✅ android/media.py
✅ android/youtube.py

Files have been copied into the new architecture.

They still require refactoring to:

- Update imports
- Use Chronicle
- Use Vault
- Match the new architecture

Legacy folders are still kept as fallback.

---

Sprint 1 — Foundation

✅ Repository structure

✅ Chronicle

    - Logging abstraction
    - Rotating logs
    - Single initialization
    - Vault path integration


✅ Vault

    - Runtime paths
    - Configuration system
    - Backward compatibility layer
    - Runtime context


✅ Nexus

    - ADB transport
    - Public API
    - CommandResult handling
    - Error handling
    - Chronicle integration


⬜ Android Device

# Roadmap

v0.1.0

Repository

Chronicle

Vault

Nexus

Android Device

CLI

v0.2.0

Registry

Dispatcher

Executor

Arsenal

v0.3.0

Brain

Oracle

Architect

Workflow Engine

v0.4.0

Windows

Browser

Plugins

v1.0

TULSI Integration

---

# Workflow

For every module:

1. Review existing implementation.

2. Refactor.

3. Preserve functionality.

4. Improve architecture.

5. Improve imports.

6. Add typing.

7. Add logging.

8. Test.

9. Commit.

Never rewrite blindly.

---

# Git Commit Style

feat(component):

fix(component):

refactor(component):

docs(component):

test(component):

Example

feat(nexus): refactor adb transport layer

---

# AI Instructions

When continuing this project:

DO NOT rewrite everything.

DO NOT generate placeholder code.

Preserve existing functionality.

Refactor module-by-module.

Produce complete production-ready files.

Keep the project runnable after every migration.

Always explain architectural decisions.

Act as the project's software architect, not just a code generator.

Maintain consistency with all decisions documented here.

---

# Next Task

Begin implementing Chronicle.

Then Vault.

Then refactor Nexus (ADB).

Do not proceed to Brain or Arsenal until Foundation is complete.

---

Last Updated

2026-07-17