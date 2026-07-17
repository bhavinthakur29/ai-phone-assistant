from .adb import ADBController

class AppManager:
    """Handles high-level application intents and states."""
    
    # Fast-lookup map for apps where the common name isn't in the package string
    APP_MAP = {
        "notes": "com.oneplus.note",
        "messages": "com.oneplus.mms",
        "browser": "com.android.chrome",
        "maps": "com.google.android.apps.maps"
    }

    # Standard system apps we want to display in the CLI list
    UI_ALIASES = [
        "camera", "calculator", "calendar", "clock", "settings", 
        "youtube", "gallery", "phone", "contacts", "files"
    ]

    @staticmethod
    def _get_installed_packages() -> list:
        """Fetches ALL installed packages (used for the backend dynamic resolver)."""
        output = ADBController.execute("pm list packages")
        packages = []
        for line in output.splitlines():
            if line.startswith("package:"):
                packages.append(line.replace("package:", "").strip())
        return packages

    @staticmethod
    def get_available_aliases() -> list:
        """Generates a clean list of aliases for the terminal UI."""
        # The '-3' flag tells ADB to only list third-party apps
        # This completely filters out the background system services
        output = ADBController.execute("pm list packages -3")
        aliases = set()
        
        for line in output.splitlines():
            if line.startswith("package:"):
                pkg = line.replace("package:", "").strip()
                parts = pkg.split('.')
                if parts:
                    alias = parts[-1].lower()
                    if len(alias) > 2:
                        aliases.add(alias)
                        
        # Inject our explicit mapped overrides
        for custom_alias in AppManager.APP_MAP.keys():
            aliases.add(custom_alias)
            
        # Inject standard system apps we always want to see
        for ui_alias in AppManager.UI_ALIASES:
            aliases.add(ui_alias)
            
        return sorted(list(aliases))

    @staticmethod
    def _resolve_package(name_or_package: str) -> str:
        """Translates a common name to a package name dynamically."""
        name = name_or_package.lower()

        if name in AppManager.APP_MAP:
            return AppManager.APP_MAP[name]

        if "." in name:
            return name

        # We still scan ALL packages here so the engine can find system apps
        installed_packages = AppManager._get_installed_packages()
        matches = [pkg for pkg in installed_packages if name in pkg.lower()]

        if matches:
            matches.sort(key=len)
            return matches[0]

        return name_or_package

    @staticmethod
    def open_app(name_or_package: str) -> str:
        package_name = AppManager._resolve_package(name_or_package)
        return ADBController.execute(f"monkey -p {package_name} -c android.intent.category.LAUNCHER 1")

    @staticmethod
    def close_app(name_or_package: str) -> str:
        package_name = AppManager._resolve_package(name_or_package)
        return ADBController.execute(f"am force-stop {package_name}")

    @staticmethod
    def browse(url: str) -> str:
        return ADBController.execute(f"am start -a android.intent.action.VIEW -d '{url}'")