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
from axion.core.bootstrap import create_registry
from axion.core.executor import Executor
from axion.core.dispatcher import Dispatcher


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


    close = commands.add_parser(
        "close",
        help="Close application",
    )

    close.add_argument(
        "package",
    )


    commands.add_parser(
        "apps",
        help="List installed applications",
    )


    return parser



def execute_command(
    args: argparse.Namespace,
) -> None:
    """
    Execute command through Axion engine.
    """

    registry = create_registry()

    executor = Executor(
        registry
    )

    dispatcher = Dispatcher(
        executor
    )


    command = ""


    if args.platform == "android":

        if args.command == "status":

            command = "android.status"


        elif args.command == "home":

            command = "android.home"


        elif args.command == "back":

            command = "android.back"


        elif args.command == "tap":

            command = (
                f"android.tap "
                f"{args.x} "
                f"{args.y}"
            )


        elif args.command == "swipe":

            command = (
                f"android.swipe "
                f"{args.x1} "
                f"{args.y1} "
                f"{args.x2} "
                f"{args.y2} "
                f"{args.duration}"
            )


        elif args.command == "type":

            command = (
                f"android.type "
                f"{args.value}"
            )


        elif args.command == "launch":

            command = (
                f"android.launch "
                f"{args.package}"
            )


        elif args.command == "close":

            command = (
                f"android.close "
                f"{args.package}"
            )


        elif args.command == "apps":

            command = "android.apps"



    result = dispatcher.dispatch(
        command
    )


    if hasattr(result, "success"):

        if result.success:

            if result.stdout:
                print(result.stdout)

            else:
                print("Success")

        else:

            if result.stderr:
                print(result.stderr)

            else:
                print("Failed")

    else:

        print(result)



def main() -> None:
    """
    CLI entry point.
    """

    parser = create_parser()

    args = parser.parse_args()

    execute_command(
        args
    )


if __name__ == "__main__":
    main()