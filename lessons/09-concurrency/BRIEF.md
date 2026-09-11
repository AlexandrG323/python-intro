# Урок 9. Потоки, GIL, процессы, asyncio

Цель: понять, почему «просто кинуть в потоки» в Python часто не ускоряет счёт, и какой инструмент выбрать.

Это не урок Лицея — это мост для тех, кто уже видел многопоточность в C++ или async в NestJS.

## Карта

CPython держит **GIL** (Global Interpreter Lock): байткод одного процесса в каждый момент выполняет только один поток. Потоки полезны, когда ждут I/O (диск, сеть, `sleep`): GIL на это время обычно отпускается. Чистый Python-цикл по числам потоками **не** размажется по ядрам.

```
CPU-bound (крутить числа)     → multiprocessing (отдельные процессы, каждый со своим GIL)
I/O-bound, много ждать сеть   → asyncio (один поток, event loop) — как NestJS
I/O-bound, блокирующие вызовы → threading
Прошивка ESP32 / realtime     → не этот стек
Простой скрипт на один файл   → sync, без фанатизма
```

Компромиссы: процессы тяжелее (нет общей памяти «просто так», pickle между процессами). Async требует, чтобы вы не блокировали loop синхронным `time.sleep` / тяжёлым CPU. Потоки проще писать и проще словить гонку.

Не используйте `os.fork` как рецепт. Современный путь: `asyncio`, `concurrent.futures`, `multiprocessing`.

## Аналогии

- Arduino: один `loop()`, никакого GIL — железа мало, потоков нет.
- C++ `std::thread`: нет GIL, CPU-bound реально параллелится (пока вы сами не сломали data race).
- NestJS: event loop ≈ asyncio. `async/await` в TypeScript вы уже нюхали.

## Наводящие вопросы

1. Почему 4 потока, считающие сумму `range(10_000_000)`, могут быть *медленнее* одного?
2. Когда вы в whiskyindex backend ждёте Postgres — это CPU или I/O? Какой инструмент в Python был бы родственником Nest async?
3. Что общего у GIL и «одного официанта на весь зал», и где аналогия врёт?

## Упражнения

Файл `exercises/concurrency.py`. Функции **детерминированные** — не пишите бенчмарки в тестах.

- `cpu_bound_sum(n: int) -> int` — `sum(range(n))`. Для `n <= 0` вернуть `0`.
- `increment_safely(counter: dict, steps: int, lock) -> None` — `steps` раз увеличить `counter["value"]` на 1, **каждый** шаг под `lock` (`with lock:`).
- `pick_tool(task: str) -> str` — нижний регистр, первое совпадение:
  1. есть `firmware` или `microcontroller` или `esp32` → `"sync"` (в Python эту работу не параллелим);
  2. есть `http` или `download` или `api wait` → `"asyncio"`;
  3. есть `cpu` или `pixels` или `compress` → `"multiprocessing"`;
  4. есть `disk` или `blocking files` → `"threading"`;
  5. иначе `"sync"`.
- `gil_held_for(kind: str) -> bool` — `True` для `"pure-python-loop"` (GIL мешает параллелить), `False` для `"time.sleep"` и `"file-read"` (ожидание, потоки могут помочь). Иной `kind` → `ValueError`.

```bash
uv run pytest lessons/09-concurrency
```

После тестов в NOTES ответьте: «что бы я выбрал для импорта Yahoo/MOEX и что — для пересчёта 10 млн строк в чистом Python».

## Урок закрыт, когда

тесты зелёные; в NOTES — схема выбора инструмента и фраза про GIL своими словами.
