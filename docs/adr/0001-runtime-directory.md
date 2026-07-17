# ADR-0001 Runtime Directory

## Status

Accepted

## Decision

Axion stores all runtime-generated files inside `.axion/`.

## Reason

Separates source code from generated state.

Provides one location for:

- logs
- cache
- reports
- temporary files
- plugin data
- workflow state

Keeps the repository clean.

Allows complete runtime reset by deleting one folder.

## Consequences

Every subsystem must obtain runtime paths through Vault.

No module should create its own runtime directories independently.