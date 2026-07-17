# ADR-0002 Nexus Transport Layer

## Status

Accepted

## Decision

Nexus is the communication layer between Axion and external systems.

Currently, Nexus provides communication with Android devices through ADB.

Future transports may include:

- Windows APIs
- Linux system interfaces
- Browser automation
- Docker
- Cloud services
- Other external platforms

Nexus is responsible only for transport and communication.

## Responsibilities

Nexus handles:

- Communication with external systems
- Command execution
- Transport errors
- Connection handling
- Returning structured results

Nexus does not understand user intent, workflows, or business operations.

## Non-Responsibilities

Nexus must not contain:

- AI logic
- Intent parsing
- Workflow logic
- User preferences
- Device-specific business rules
- Automation decisions

Higher-level modules decide what should happen.

Nexus only handles how communication happens.

## Reason

Separating communication from higher-level logic provides:

- Replaceable transport implementations
- Easier testing
- Cleaner architecture
- Support for multiple platforms
- Prevention of tightly coupled modules

Higher-level abstractions such as Devices and Arsenal can operate without knowing transport implementation details.

## Consequences

All external communication must go through Nexus.

No module may:

- Directly execute external commands
- Call subprocess APIs for external systems
- Bypass Nexus communication layers

The dependency flow is:

CLI / Brain / Workflows

↓

Devices / Arsenal

↓

Nexus

↓

External Systems

## Architectural Rule

Nexus must remain replaceable.

Replacing ADB with another communication mechanism should not require changes to Devices, Arsenal, Brain, or Workflow Engine.

Nexus should expose stable communication interfaces while keeping transport-specific implementation details internal.