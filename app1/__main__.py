"""Main app."""

import sys
import typing as t

from stateless.console import Console
from stateless.effect import Effect, depend
from stateless.runtime import Runtime


def print_(value: str) -> Effect[Console, t.Never, None]:
    """Print."""
    console = yield from depend(Console)  # depend returns abilities
    console.print(value)


def input_(value: str) -> Effect[Console, t.Never, str]:
    """Print."""
    console = yield from depend(Console)  # depend returns abilities
    return console.input(value)


def app() -> Effect[Console, t.Never, int]:
    "App."
    yield from print_("start up")
    yield from print_("ending")
    a = yield from input_("what is your name?")
    yield from print_(f"hello {a}")
    return 0


def main() -> int:
    "main function." ""
    run = Runtime()
    run.use(Console()).run(app())
    return 0


if __name__ == "__main__":
    try:
        val = main()
    except EOFError:
        val = -1
    except KeyboardInterrupt:
        val = -1
    except RuntimeError:
        val = -1
    sys.exit(val)
