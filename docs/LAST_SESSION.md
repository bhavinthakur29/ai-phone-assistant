Axion Android automation progress:

Completed:
- Created modular CLI -> Dispatcher -> Executor -> Registry architecture.
- Added Android input actions:
  - android.home
  - android.back
  - android.tap
  - android.swipe
  - android.type
- Added Android application actions:
  - android.launch
  - android.close
  - android.apps
- Added Oracle layer foundation:
  - axion/oracle/android/
  - AndroidScreenOracle for device observation.
- CLI supports mixed result types:
  - CommandResult actions
  - Data-returning oracle actions

Current architecture:

CLI
 |
 Dispatcher
 |
 Executor
 |
 Action Registry
 |
 Arsenal (actions)
 |
 Devices (hardware abstraction)
 |
 Nexus (ADB transport)

New layer being added:
Oracle
 |
 AndroidScreenOracle
 |
 ADB queries:
   - wm size
   - wm density

Next milestone:
Add android screenshot capability.

Purpose:
Enable AI perception by allowing Axion to capture and analyse device state rather than only execute coordinates.