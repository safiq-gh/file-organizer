import pytest
from fsort.grouper import group_files
from fsort.strategies import registry


def test_duplicate_group_name_fails(monkeypatch):
    class StrategyA:
        group_name = "Dup"

        def accepts(self, file):
            return False

    class StrategyB:
        group_name = "Dup"

        def accepts(self, file):
            return True

    # Override the registry for this test only
    monkeypatch.setattr(
        registry,
        "StrategyList",
        [StrategyA, StrategyB],
    )

    # Startup must fail before grouping
    with pytest.raises(AttributeError):
        group_files([])

def test_multiple_fallback_fails(monkeypatch):
    class StrategyA:
        group_name = "Dup"
        def accepts(self, file):
            return True

    class StrategyB:
        group_name = "Cup"
        def accepts(self, file):
            return True

    # Override the registry for this test only
    monkeypatch.setattr(
        registry,
        "StrategyList",
        [StrategyA, StrategyB],
    )

    # Startup must fail before grouping
    with pytest.raises(AttributeError):
        group_files([])

def test_no_fallback_fails(monkeypatch):
    class StrategyA:
        group_name = "Cup"
        def accepts(self, file):
            return False

    class StrategyB:
        group_name = "Dup"
        def accepts(self, file):
            return False

    # Override the registry for this test only
    monkeypatch.setattr(
        registry,
        "StrategyList",
        [StrategyA, StrategyB],
    )

    # Startup must fail before grouping
    with pytest.raises(AttributeError):
        group_files([])

def test_fallback_must_be_last_fails(monkeypatch):
    class StrategyA:
        group_name = "Cup"
        def accepts(self, file):
            return False

    class StrategyB:
        group_name = "Dup"
        def accepts(self, file):
            return True

    # Override the registry for this test only
    monkeypatch.setattr(
        registry,
        "StrategyList",
        [StrategyB, StrategyA],
    )

    # Startup must fail before grouping
    with pytest.raises(AttributeError):
        group_files([])

def test_return_of_accepts_fail(monkeypatch):
    class StrategyA:
        group_name = "Cup"
        def accepts(self, file) -> bool:
            return 1

    class StrategyB:
        group_name = "Dup"
        def accepts(self, file) -> bool:
            return "yes"

    # Override the registry for this test only
    monkeypatch.setattr(
        registry,
        "StrategyList",
        [StrategyA, StrategyB],
    )

    # Startup must fail before grouping
    with pytest.raises(AttributeError):
        group_files([])

@pytest.mark.parametrize(
    "BrokenStrategy",
    [
        # missing group_name
        type(
            "NoGroupName",
            (),
            {"accepts": lambda self, file: False},
        ),
        # empty group_name
        type(
            "EmptyGroupName",
            (),
            {"group_name": "", "accepts": lambda self, file: False},
        ),
        # non-string group_name
        type(
            "NonStringGroupName",
            (),
            {"group_name": 123, "accepts": lambda self, file: False},
        ),
    ],
)
def test_invalid_group_name_fails(BrokenStrategy,monkeypatch):
    class ValidFallback:
        group_name = "Fallback"
        def accepts(self, file):
            return True

    monkeypatch.setattr(
        registry,
        "StrategyList",
        [BrokenStrategy, ValidFallback],
    )

    # This relies on the real registry behavior:
    # group_files instantiates strategies from registry order
    # so we pass both strategies directly
    with pytest.raises(AttributeError):
        group_files([])
