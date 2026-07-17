# ADR-0001 Runtime Directory

## Status

Accepted

## Decision

Axion uses `.axion/` as the single runtime directory for all generated and mutable application state.

Source code, configuration templates, and static resources must remain outside this directory.

## Reason

Separating runtime state from source code provides:

- Cleaner repository structure
- Easier debugging and maintenance
- Simple runtime cleanup and reset
- Clear ownership of generated files

The `.axion/` directory contains:

- Logs
- Cache
- Reports
- Temporary files
- Plugin data
- Workflow state
- Runtime metadata

A complete runtime reset can be performed by removing the `.axion/` directory.

## Consequences

All subsystems must obtain runtime paths through Vault.

No module may create runtime directories independently.

Vault is the single source of truth for runtime filesystem locations.