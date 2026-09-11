from pathlib import Path


def load_prices(path: Path) -> list[dict]:
    raise NotImplementedError


def price_in_year(rows: list[dict], product: str, year: int) -> float:
    raise NotImplementedError


def parse_year(text: str) -> int:
    raise NotImplementedError


def safe_price(
    rows: list[dict],
    product: str,
    year: int,
    default: float = 0.0,
) -> float:
    raise NotImplementedError
