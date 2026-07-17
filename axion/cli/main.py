"""
Axion command-line interface.

Responsibilities:
- Parse user commands.
- Call Axion abstractions.
- Display results.

The CLI contains no automation logic.
"""

from __future__ import annotations

import argparse

from axion.chronicle import get_logger
from axion.devices import AndroidDevice


logger = get_logger(__name__)


def create_parser() -> argparse.ArgumentParser:
    """
    Create Axion CLI parser.
    """

    parser = argparse.ArgumentParser(
        prog="axion",
        description="Axion automation engine",
    )

    platforms = parser.add_subparsers(
        dest="platform",
        required=True,
    )

    android = platforms.add_parser(
        "android",
        help="Android device commands",
    )

    commands = android.add_subparsers(
        dest="command",
        required=True,
    )

    commands.add_parser(
        "status",
        help="Check Android connection",
    )

    commands.add_parser(
        "home",
        help="Press home button",
    )

    commands.add_parser(
        "back",
        help="Press back button",
    )

    tap = commands.add_parser(
        "tap",
        help="Tap screen coordinate",
    )

    tap.add_argument(
        "x",
        type=int,
    )

    tap.add_argument(
        "y",
        type=int,
    )

    swipe = commands.add_parser(
        "swipe",
        help="Swipe screen",
    )

    swipe.add_argument(
        "x1",
        type=int,
    )

    swipe.add_argument(
        "y1",
        type=int,
    )

    swipe.add_argument(
        "x2",
        type=int,
    )

    swipe.add_argument(
        "y2",
        type=int,
    )

    swipe.add_argument(
        "--duration",
        type=int,
        default=300,
    )

    text = commands.add_parser(
        "type",
        help="Type text",
    )

    text.add_argument(
        "value",
    )

    launch = commands.add_parser(
        "launch",
        help="Launch application",
    )

    launch.add_argument(
        "package",
    )

    return parser


def execute_command(
    args: argparse.Namespace,
) -> None:
    """
    Execute CLI command.
    """

    device = AndroidDevice()

    if args.platform != "android":
        return

    if args.command == "status":

        print(
            "Connected"
            if device.is_connected()
            else "Not connected"
        )

    elif args.command == "home":

        result = device.home()
        print(result.success)

    elif args.command == "back":

        result = device.press_back()
        print(result.success)

    elif args.command == "tap":

        result = device.tap(
            args.x,
            args.y,
        )

        print(result.success)

    elif args.command == "swipe":

        result = device.swipe(
            args.x1,
            args.y1,
            args.x2,
            args.y2,
            args.duration,
        )

        print(result.success)

    elif args.command == "type":

        result = device.type_text(
            args.value,
        )

        print(result.success)

    elif args.command == "launch":

        result = device.launch_app(
            args.package,
        )

        print(result.success)


def main() -> None:
    """
    CLI entry point.
    """

    parser = create_parser()

    args = parser.parse_args()

    execute_command(args)


if __name__ == "__main__":
    main()