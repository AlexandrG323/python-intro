from types import SimpleNamespace

from basket import Basket, Product, total_of


def test_product_discount_returns_new() -> None:
    original = Product("jameson", 100.0)
    cheaper = original.with_discount(10)
    assert cheaper == Product("jameson", 90.0)
    assert original.price == 100.0
    assert cheaper is not original


def test_basket_add_total_len() -> None:
    basket = Basket()
    assert len(basket) == 0
    assert basket.total() == 0.0
    basket.add(Product("jameson", 800.0))
    basket.add(Product("cola", 50.0))
    assert len(basket) == 2
    assert basket.total() == 850.0


def test_total_of_duck_typing() -> None:
    items = [
        Product("cola", 50.0),
        SimpleNamespace(price=10.5),
    ]
    assert total_of(items) == 60.5
    assert total_of([]) == 0.0
