from pathlib import Path


def yearly_totals(path: Path) -> dict[int, float]:
    raise NotImplementedError


def max_increase(path: Path) -> tuple[str, float]:
    raise NotImplementedError


def format_report(totals: dict[int, float]) -> str:
    raise NotImplementedError


def when_not_python(job: str) -> bool:
    raise NotImplementedError
