# Урок 7. Модули, файлы, ошибки

Цель: читать файлы через `pathlib`, разбирать CSV, бросать и ловить исключения так, как вы уже делаете `try/catch` в TypeScript.

## Карта

`Path` из `pathlib` — современный путь (не склеивайте строки через `os.path.join` без нужды).

```
path.read_text()     весь файл как str
path.open()          итерация по строкам / csv
```

`csv.DictReader` даёт словари с ключами из заголовка. Числа из CSV приходят **строками** — их нужно привести к `int` / `float`.

Исключение — объект ошибки. `raise ValueError("...")`. `try/except` ловит. Ловите конкретный тип, не голый `except:`.

```
try:
    ...
except KeyError:
    запасной путь
```

В C++ исключение + RAII. В Python `with path.open() as f:` закрывает файл (контекстный менеджер ≈ RAII для ресурса).

Модуль = файл. Пакет = папка с модулями. Мы пока без сложных пакетов: функции в одном файле, данные рядом в `data/`.

## Аналогии

- whiskyindex: цены в Postgres. Здесь учебный срез — CSV «продукт, год, цена».
- TypeScript: `throw new Error` / `catch (e)`. Нет типов исключений в сигнатуре как в Java; в Python тоже нет checked exceptions.
- C++: `throw`, `catch`, деструктор закроет файл; здесь — `with`.

## Наводящие вопросы

1. Почему `except Exception` почти всегда хуже `except KeyError`?
2. Чем `Path(__file__).resolve().parent` полезен в тестах и скриптах?
3. Что будет, если забыть `int(row["year"])`?

## Упражнения

Файл `exercises/prices.py`. Тесты кладут путь к `data/prices.csv`.

Строки CSV: заголовок `product,year,price`. Год → `int`, цена → `float`.

- `load_prices(path: Path) -> list[dict]` — список словарей с ключами `product` (str), `year` (int), `price` (float). Порядок как в файле.
- `price_in_year(rows, product: str, year: int) -> float` — цена. Если пары нет — `KeyError` (сообщение любое).
- `parse_year(text: str) -> int` — `int(text)`, при неудаче `ValueError`.
- `safe_price(rows, product, year, default: float = 0.0) -> float` — как `price_in_year`, но при `KeyError` вернуть `default`.

```bash
uv run pytest lessons/07-modules-files-errors
```

## Урок закрыт, когда

тесты зелёные; в NOTES — зачем `with` и чем `KeyError` отличается от `ValueError`.
