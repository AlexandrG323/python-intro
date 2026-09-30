import csv
from pathlib import Path


def load_prices(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows.append(
                {
                    "product": row["product"],
                    "year": int(row["year"]),
                    "price": float(row["price"]),
                }
            )
    return rows


def price_in_year(rows: list[dict], product: str, year: int) -> float:
    for row in rows:
        if row["product"] == product and row["year"] == year:
            return row["price"]
    raise KeyError(f"Product '{product}' for year '{year}' is missing")


def parse_year(text: str) -> int:
    return int(text)


def safe_price(
    rows: list[dict],
    product: str,
    year: int,
    default: float = 0.0,
) -> float:
    try:
        return price_in_year(rows, product, year)
    except KeyError:
        return default
