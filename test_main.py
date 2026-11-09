from main import TOOLS, calculator


def test_calculator_registered():
    assert "calculator" in TOOLS


def test_calculator_counts():
    assert calculator("2 + 2 * 2") == 6
