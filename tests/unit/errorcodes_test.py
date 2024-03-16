from __future__ import annotations

from mypypp.errorcodes import DEPRECATED


def test_deprecated() -> None:
    assert DEPRECATED.code == "deprecated"
    assert DEPRECATED.category == "General"
    assert DEPRECATED.default_enabled
    assert DEPRECATED.sub_code_of is None
