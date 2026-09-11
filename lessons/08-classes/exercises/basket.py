from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    name: str
    price: float

    def with_discount(self, percent: float) -> "Product":
        raise NotImplementedError


class Basket:
    def __init__(self) -> None:
        self._items: list[Product] = []

    def add(self, product: Product) -> None:
        raise NotImplementedError

    def total(self) -> float:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


def total_of(items) -> float:
    raise NotImplementedError
