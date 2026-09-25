def unique_sorted(xs: list[str]) -> list[str]:
    unique = set(xs)
    return sorted(unique)


def word_counts(text: str) -> dict[str, int]:
    words = text.split()
    og = dict.fromkeys(set(words), 0)
    for word in words:
        og[word] += 1
    return og


def top_n(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    xs = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return xs[:n]


def flatten(matrix: list[list[int]]) -> list[int]:
    flatMat = list[int]()
    for n in matrix:
        flatMat.extend(n)
    return flatMat


def even_squares(xs: list[int]) -> list[int]:
    squares = list[int]()
    for n in xs:
        if n % 2 == 0:
            squares.append(n * n)
    return squares


def total_by_year(rows: list[tuple[str, int, float]]) -> dict[int, float]:
    sales = dict.fromkeys((row[1] for row in rows), 0)
    for r in rows:
        sales[r[1]] += r[2]
    return sales
