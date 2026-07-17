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

    return parser


def build_dispatcher() -> Dispatcher:
    """
    Create Axion execution pipeline.

    CLI only initializes components.
    """

    registry = create_registry()

    executor = Executor(
        registry
    )

    return Dispatcher(
        executor
    )


def create_command(
    args: argparse.Namespace,
) -> str:
    """
    Convert CLI arguments into Axion commands.

    CLI does not execute actions.
    It only translates user input.
    """

    if args.platform != "android":
        return ""

    if args.command == "status":
        return "android.status"

    if args.command == "home":
        return "android.home"

    if args.command == "back":
        return "android.back"

    if args.command == "tap":
        return (
            f"android.tap "
            f"{args.x} "
            f"{args.y}"
        )

    if args.command == "swipe":
        return (
            f"android.swipe "
            f"{args.x1} "
            f"{args.y1} "
            f"{args.x2} "
            f"{args.y2} "
            f"{args.duration}"
        )

    if args.command == "type":
        return (
            f"android.type "
            f"{args.value}"
        )

    if args.command == "launch":
        return (
            f"android.launch "
            f"{args.package}"
        )

    return ""


def display_result(
    result: object,
) -> None:
    """
    Display execution result.

    Supports different action return types.
    """

    if hasattr(result, "success"):

        if result.success:
            print("Success")
        else:
            print("Failed")

        return

    print(result)


def execute_command(
    args: argparse.Namespace,
) -> None:
    """
    Execute CLI command through Axion engine.
    """

    dispatcher = build_dispatcher()

    command = create_command(
        args
    )

    if not command:
        print(
            "Unknown command"
        )
        return

    result = dispatcher.dispatch(
        command
    )

    display_result(
        result
    )


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