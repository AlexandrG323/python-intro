from pathlib import Path

from report import format_report, max_increase, when_not_python, yearly_totals

DATA = Path(__file__).resolve().parents[1] / "data" / "prices.csv"


def test_yearly_totals() -> None:
    assert yearly_totals(DATA) == {2007: 950.0, 2024: 2330.0}


def test_max_increase() -> None:
    name, change = max_increase(DATA)
    assert name == "cola"
    assert change == 1.8


def test_format_report() -> None:
    text = format_report({2024: 2330.0, 2007: 950.0})
    assert text == "2007: 950.00\n2024: 2330.00"


def test_format_report_empty() -> None:
    assert format_report({}) == ""


def test_when_not_python() -> None:
    assert when_not_python("ESP32 firmware blink") is True
    assert when_not_python("Hard realtime motor loop") is True
    assert when_not_python("Embedded sensor firmware") is True
    assert when_not_python("Rewrite a GPU kernel inner loop") is True
    assert when_not_python("CSV glue script for an LLM prototype") is False
    assert when_not_python("one-off notebook") is False
