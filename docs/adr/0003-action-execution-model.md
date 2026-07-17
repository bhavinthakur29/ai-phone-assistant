# ADR-0003 Action Execution Model

## Status

Accepted


## Decision

Axion uses Actions as the primary execution unit.

All executable operations must be represented as Actions.

Examples:

- HomeAction
- BackAction
- TapAction
- LaunchAppAction


## Reason

Actions provide a common execution interface between:

- CLI
- Brain
- Workflows
- Plugins
- External APIs


This prevents different interfaces from directly controlling devices.


## Consequences

The execution flow becomes:

Request

↓

Executor

↓

Action

↓

Device

↓

Nexus


CLI and Brain must not directly call device methods.

The Executor is responsible for action execution.