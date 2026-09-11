# Урок 4. Условия и циклы

Цель: перенести уже знакомые `if` / `for` / `while` на синтаксис Python и освоить современный `match`.

## Карта

- Блоки задаёт **отступ**, не `{}`. Смешивать табы и пробелы нельзя.
- `elif`, не `else if`.
- `for x in xs` — итерация по коллекции, не «счётчик как в C `for (int i=…)`». Счётчик даёт `range`.
- `range(start, stop)` **не включает** `stop` (как полуинтервал).
- `while` — когда не знаете заранее, сколько шагов (как ждать датчик на Arduino).
- `for` / `else`: ветка `else` у цикла выполняется, если **не** было `break`. Это не «иначе если пусто» в смысле if.
- `match` — структурное сопоставление (3.10+). Для кода 3.13 это стандарт, не словарь-имитация switch.

Истина в условиях: `0`, `""`, `[]`, `None`, `False` — ложны. Непустые коллекции — истинны. Явная проверка лучше, чем полагаться на это вслепую.

## Аналогии

- Arduino `loop()` + `if (t >= 23)` в `Servo-Arduino.ino` — тот же if, другой синтаксис.
- C++ `switch` по `int` vs Python `match` (можно разбирать структуру, не только число).
- TypeScript `for...of` ≈ Python `for x in xs`.

## Наводящие вопросы

1. Чем `for i in range(len(xs))` хуже `for x in xs`, и когда индекс всё-таки нужен?
2. Когда `while True` уместен, а когда это вечный цикл без `break` как забытый `loop()`?
3. Почему `for-else` путают все, кто пришёл из C++?

## Упражнения

Файл `exercises/control_flow.py`:

- `fizzbuzz(n: int) -> str` — `"FizzBuzz"` если n делится на 3 и 5, `"Fizz"` на 3, `"Buzz"` на 5, иначе строка самого числа (`str(n)`). Порядок проверок важен.
- `countdown(n: int) -> list[int]` — через `while`: `[n, n-1, …, 1]`. Для `n <= 0` — пустой список.
- `sum_range(start: int, stop: int) -> int` — сумма `range(start, stop)` (stop не входит).
- `classify_status(code: int) -> str` — через `match` по `code // 100`: `2 → "success"`, `3 → "redirect"`, `4 → "client_error"`, `5 → "server_error"`, иначе `"other"`.
- `first_even(xs: list[int]) -> int | None` — первое чётное; если нет — `None`. Имеет смысл попробовать `for`/`else`.

```bash
uv run pytest lessons/04-control-flow
```

## Урок закрыт, когда

тесты зелёные; в NOTES — своими словами `range` и `match`.
