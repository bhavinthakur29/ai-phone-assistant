# AXION CONTEXT

> This file is the architectural source of truth for Axion.
> It explains what Axion is, how it is designed, and the rules that must be followed during development.

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

It is NOT an Android automation tool only.

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

Axion is AI-agnostic.

Axion does not contain intelligence itself.

AI assistants such as TULSI will use Axion as an execution engine.

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

Axion follows strict modular architecture.

Core principles:

- Every subsystem has one responsibility.
- Avoid god classes.
- Keep components replaceable.
- Separate intelligence from execution.
- Separate business logic from communication.
- Prefer composition over inheritance.
- Keep modules independently testable.

---

# System Architecture

High-level flow:

Brain

↓

Core Engine

↓

Arsenal Actions

↓

Devices

↓

Nexus

↓

External Systems


---

# Components


## Brain

Purpose:

- Intent understanding
- NLP
- Speech processing
- AI integration

Responsibilities:

- Understand requests.
- Convert intent into executable actions.

Never:

- Execute device operations.
- Communicate directly with hardware.


---

## Oracle

Purpose:

Knowledge layer.

Contains:

- Application metadata
- Package names
- Aliases
- Device capabilities
- User preferences

Oracle provides information only.

Oracle does not execute actions.


---

## Core

Purpose:

Execution management.

Contains:

- Registry
- Dispatcher
- Executor

Responsibilities:

- Manage actions.
- Route requests.
- Execute workflows.


---

## Arsenal

Purpose:

Action library.

Contains executable actions.

Examples:

- OpenAppAction
- CloseAppAction
- TapAction
- SwipeAction
- ScreenshotAction
- MediaAction

Actions define what Axion can do.


---

## Devices

Purpose:

High-level device abstraction.

Examples:

- AndroidDevice
- WindowsDevice
- LinuxDevice

Responsibilities:

- Provide simple interfaces.
- Hide transport details.
- Delegate communication to Nexus.

Example:

AndroidDevice

↓

Nexus

↓

ADB


Devices must never contain low-level communication logic.


---

## Nexus

Purpose:

Communication layer.

Current:

- ADB

Future:

- Win32
- Browser automation
- Docker
- Linux interfaces
- Cloud APIs


Responsibilities:

- Communicate with external systems.
- Return structured results.


Never:

- Contain business logic.
- Understand user intent.
- Decide actions.


---

## Vault

Purpose:

Configuration and runtime environment.

Provides:

- Settings
- Runtime paths
- Environment information
- Shared configuration


All runtime paths must come from Vault.


---

## Chronicle

Purpose:

Centralized logging system.

Rules:

- All modules use Chronicle.
- No print() in production.
- No independent logging systems.


---

## Sentinel

Purpose:

Monitoring.

Responsibilities:

- Health checks
- Failure detection
- Watchdog


---

## CLI

Purpose:

Human interface.

Responsibilities:

- Parse commands.
- Initialize Axion.
- Call internal APIs.
- Display results.


CLI must contain no business logic.


---

# Dependency Rules

Allowed:

Brain -> Oracle

Brain -> Vault

Core -> Arsenal

Executor -> Devices

Devices -> Nexus

All modules -> Chronicle

All modules -> Vault


Not Allowed:

Nexus -> Brain

Chronicle -> Brain

Oracle -> CLI

CLI -> Nexus


---

# Runtime Rules

All runtime-generated files belong inside:

.axion/


Examples:

- Logs
- Cache
- Reports
- Temporary files
- Plugin data
- Workflow state


No module creates runtime directories independently.

Vault controls runtime paths.


---

# Coding Standards

Python:

3.12+


Rules:

- Type hints everywhere.
- Public classes/functions require docstrings.
- Use pathlib.
- No wildcard imports.
- No print() in production.
- Use Chronicle logging.
- Explicit exceptions.
- One responsibility per file.
- Avoid circular imports.


---

# Import Style

Preferred:

from axion.chronicle import get_logger

from axion.vault import settings


Avoid:

from axion.chronicle.chronicle import Chronicle


---

# Naming Convention

Products:

Axion

TULSI


Subsystems:

Brain

Oracle

Arsenal

Nexus

Chronicle

Vault

Sentinel


Actions:

OpenAppAction

TapAction

SwipeAction


Models:

Device

Workflow

ActionRequest


---

# Development Workflow

For every module:

1. Review existing implementation.
2. Refactor carefully.
3. Preserve functionality.
4. Improve architecture.
5. Improve imports.
6. Add typing.
7. Add logging.
8. Test.
9. Commit.


Never rewrite blindly.


---

# Git Commit Convention

feat(component):

fix(component):

refactor(component):

docs(component):

test(component):


Example:

feat(nexus): refactor adb transport layer


---

# Architecture Decision Records

Location:

docs/adr/


Current ADRs:

0001-runtime-directory.md

0002-nexus-transport-layer.md


---

# Roadmap


## v0.1.0 Foundation

- Repository structure
- Chronicle
- Vault
- Nexus
- Devices
- CLI


## v0.2.0 Execution Engine

- Registry
- Dispatcher
- Executor
- Arsenal
- Action system
- Workflow engine


## v0.3.0 Intelligence Layer

- Brain
- Oracle
- AI integration
- Speech processing
- Intent understanding


## v0.4.0 Platform Expansion

- Windows
- Browser
- Linux
- Docker
- Home Assistant
- Plugins


## v1.0.0 TULSI Integration

- TULSI integration
- Plugin ecosystem
- Stable public API
- External integrations