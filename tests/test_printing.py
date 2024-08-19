"""test."""

import pytest
import stateless.errors
import stateless.runtime

from app1.__main__ import print_


def test_print() -> None:
    """Test print_."""
    with pytest.raises(stateless.errors.MissingAbilityError) as _:
        stateless.runtime.Runtime().run(print_("test"))
