import sys
import textwrap
from assistant.dispatcher import CommandDispatcher
from android.apps import AppManager

def main():
    print("Loading Axion Engine...")
    dispatcher = CommandDispatcher()
    
    print("=================================")
    print("    AXION ENGINE - MILESTONE 2   ")
    print("=================================")
    
    print("Scanning Android device for installed packages...\n")
    aliases = AppManager.get_available_aliases()
    
    print("--- Available App Aliases (Use with 'open' or 'close') ---")
    # Wrap the aliases into a neat paragraph max 80 characters wide
    formatted_aliases = textwrap.fill(", ".join(aliases), width=80)
    print(formatted_aliases)
    print("-" * 58)
    
    print("\n--- Available Core Commands ---")
    print("  - home, back, power")
    print("  - tap <x> <y>, swipe <x1> <y1> <x2> <y2>")
    print("  - scroll <up/down/left/right>")
    print("  - type <text>, clear")
    print("  - play, next, yt <query>")
    print("  - battery, screen")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("axion> ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit']:
                print("Shutting down engine...")
                sys.exit(0)
            
            response = dispatcher.dispatch(user_input)
            print(f"[{response}]\n")

        except KeyboardInterrupt:
            print("\nShutting down engine...")
            sys.exit(0)

if __name__ == "__main__":
    main()