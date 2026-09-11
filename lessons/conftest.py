"""Put each lesson's exercises/ on sys.path so tests can import stubs by module name."""

import sys
from pathlib import Path

_lessons_root = Path(__file__).resolve().parent
for _exercises in sorted(_lessons_root.glob("*/exercises")):
    _path = str(_exercises)
    if _path not in sys.path:
        sys.path.insert(0, _path)
