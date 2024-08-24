"""test."""

import typing as t

import pytest
import stateless.console
import stateless.effect as e
import stateless.errors
import stateless.runtime

from app1.__main__ import print_


def test_print() -> None:
    """Test print_."""
    effect: e.Effect[stateless.console.Console, t.Never, None] = print_("test")
    with pytest.raises(stateless.errors.MissingAbilityError) as _:
        stateless.runtime.Runtime().run(effect)
