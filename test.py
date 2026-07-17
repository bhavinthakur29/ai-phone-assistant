"""
Manual AndroidDevice integration test.

Run:
python test.py
"""

from axion.devices import AndroidDevice


def main() -> None:
    device = AndroidDevice()

    print("Checking connection...")

    result = device.connect()

    print("\nADB Result:")
    print(result.stdout)

    if not device.is_connected():
        print("No Android device connected.")
        return

    print("\nAndroid device connected.")

    print("\nTesting home button...")
    result = device.home()

    print(result.success)

    print("\nTesting back button...")
    result = device.press_back()

    print(result.success)

    print("\nTesting tap...")

    result = device.tap(
        500,
        500,
    )

    print(result.success)


if __name__ == "__main__":
    main()