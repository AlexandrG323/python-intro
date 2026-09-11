# Python Intro

Десять занятий — мост к [Яндекс Лицею](https://lyceum.yandex.ru/python): вы уже пишете на C++/Arduino и TypeScript (whiskyindex), здесь учитесь думать на Python.

Тикет: [SKUF-60](https://alex-lessons.atlassian.net/browse/SKUF-60). Это не продукт и не монорепозиторий вроде whiskyindex — только уроки, заготовки и тесты.

## Как заниматься

1. Открой этот репозиторий в Cursor.
2. Напиши агенту: **«какое следующее задание»**.
3. Разберите `BRIEF.md` текущего урока вопросами, не готовым кодом.
4. Допиши функции в `lessons/NN-…/exercises/`.
5. Проверь: `uv run pytest lessons/NN-slug`.
6. Своими словами заполни `NOTES.md`, допиши строку в `session.md`.

Правила ментора: [AGENTS.md](AGENTS.md). Прогресс: [PROGRESS.md](PROGRESS.md).

## Среда на этой машине

Системный `/usr/bin/python3` (3.9.6 от macOS) **не используем**.

Уже установлено:

| Что | Зачем |
| --- | --- |
| Homebrew `uv` 0.12 | Менеджер Python: интерпретатор, `.venv`, пакеты. Замена pyenv + pip + venv. |
| CPython **3.13.15** | Через `uv python install 3.13`, не через `brew install python`. |
| `.venv` в корне | Локальное окружение проекта. |
| pytest, ruff | Тесты как контракт; форматтер/линтер. |

Не ставили: Anaconda, pyenv, Jupyter, `python@3.13` из Homebrew (второй интерпретатор не нужен — Cursor берёт `.venv`).

Команды из корня репозитория:

```bash
source .venv/bin/activate   # необязательно, если зовёте uv run
uv run python --version     # Python 3.13.x
uv run pytest lessons/01-why-python
uv run pytest               # все уроки сразу — обычно не надо
uv run ruff check lessons
```

Интерпретатор Cursor: `.venv/bin/python` (см. `.vscode/settings.json`).

Если открыли новый терминал и `uv` не находится: `eval "$(/opt/homebrew/bin/brew shellenv)"`.

## Уроки

| День | Папка | О чём |
| --- | --- | --- |
| 1 | [lessons/01-why-python](lessons/01-why-python) | Чем Python отличается и зачем его берут |
| 2 | [lessons/02-how-python-runs](lessons/02-how-python-runs) | Как выполняется код: REPL, скрипт, import |
| 3 | [lessons/03-names-types](lessons/03-names-types) | Имена, типы, изменяемость |
| 4 | [lessons/04-control-flow](lessons/04-control-flow) | Условия, циклы, `match` |
| 5 | [lessons/05-collections](lessons/05-collections) | list, tuple, dict, set |
| 6 | [lessons/06-functions](lessons/06-functions) | Функции, область видимости |
| 7 | [lessons/07-modules-files-errors](lessons/07-modules-files-errors) | Модули, файлы, ошибки |
| 8 | [lessons/08-classes](lessons/08-classes) | Классы vs C++, dataclasses |
| 9 | [lessons/09-concurrency](lessons/09-concurrency) | Потоки, GIL, процессы, asyncio |
| 10 | [lessons/10-stdlib-and-why-python-wins](lessons/10-stdlib-and-why-python-wins) | stdlib и где Python выигрывает |

Эталонов нет. Спецификация — тесты и `BRIEF.md`.

## Язык

Сводки и BRIEF — на русском. Имена файлов и код — на английском.
