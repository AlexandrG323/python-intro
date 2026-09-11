from pathlib import Path

import pytest

from prices import load_prices, parse_year, price_in_year, safe_price

DATA = Path(__file__).resolve().parents[1] / "data" / "prices.csv"


def test_load_prices() -> None:
    rows = load_prices(DATA)
    assert rows == [
        {"product": "jameson", "year": 2007, "price": 800.0},
        {"product": "jameson", "year": 2024, "price": 2100.0},
        {"product": "cola", "year": 2007, "price": 50.0},
        {"product": "cola", "year": 2024, "price": 140.0},
    ]


def test_price_in_year() -> None:
    rows = load_prices(DATA)
    assert price_in_year(rows, "jameson", 2007) == 800.0
    assert price_in_year(rows, "cola", 2024) == 140.0


def test_price_in_year_missing() -> None:
    rows = load_prices(DATA)
    with pytest.raises(KeyError):
        price_in_year(rows, "apple", 2007)


def test_parse_year() -> None:
    assert parse_year("2024") == 2024
    with pytest.raises(ValueError):
        parse_year("twenty")


def test_safe_price() -> None:
    rows = load_prices(DATA)
    assert safe_price(rows, "jameson", 2024) == 2100.0
    assert safe_price(rows, "apple", 2007) == 0.0
    assert safe_price(rows, "apple", 2007, default=99.5) == 99.5
