# Прогресс

Текущий урок: **06-functions**

Статусы: `not_started` → `in_progress` → `review` → `done`.

Агент не перескакивает вперёд: пока урок не `done`, следующий не разбираем как основную тему.

| Урок | Тема | Статус |
| --- | --- | --- |
| [01-why-python](lessons/01-why-python) | Почему Python | done |
| [02-how-python-runs](lessons/02-how-python-runs) | Как выполняется код | done |
| [03-names-types](lessons/03-names-types) | Имена, типы, изменяемость | done |
| [04-control-flow](lessons/04-control-flow) | Условия и циклы | done |
| [05-collections](lessons/05-collections) | Коллекции | done |
| [06-functions](lessons/06-functions) | Функции | in_progress |
| [07-modules-files-errors](lessons/07-modules-files-errors) | Модули, файлы, ошибки | not_started |
| [08-classes](lessons/08-classes) | Классы | not_started |
| [09-concurrency](lessons/09-concurrency) | Потоки и GIL | not_started |
| [10-stdlib-and-why-python-wins](lessons/10-stdlib-and-why-python-wins) | stdlib и зачем Python в проде | not_started |

Урок закрыт, когда:

1. `uv run pytest lessons/NN-slug` зелёный;
2. `NOTES.md` заполнен учеником своими словами;
3. агент дописал строку занятия в `session.md`.
