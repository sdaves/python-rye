"""Main app."""

import sys
import typing as t

from stateless import effect as e
from stateless.console import Console
from stateless.runtime import Runtime


def print_(value: str) -> e.Effect[Console, t.Never, None]:
    """Print."""
    console = yield from e.depend(Console)  # depend returns abilities
    console.print(value)


def input_(value: str) -> e.Effect[Console, t.Never, str]:
    """Print."""
    console = yield from e.depend(Console)  # depend returns abilities
    return console.input(value)


@e.throws(ZeroDivisionError, ValueError)
def divide() -> e.Effect[Console, t.Never, None]:
    "App."
    yield from print_("start up")
    first = yield from input_("what is the first number? ")
    second = yield from input_("what is the first number? ")
    ans = str(float(first) / float(second))
    yield from print_(f"{first} / {second} = {ans}")


def app() -> e.Effect[Console, t.Never, int]:
    """App."""
    yield from print_("start up")
    result = yield from e.catch(divide)()

    match result:
        case ZeroDivisionError():
            yield from print_("ending zero division error")
            return -1
        case _:
            yield from print_("ending success")
            return 0


def main() -> int:
    "main function." ""
    run: Runtime = Runtime()
    return run.use(Console()).run(app())


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
