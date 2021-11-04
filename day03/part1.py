from typing import Iterable, List

from day03.common import TREE, read_map


def solve(filename: str) -> int:
    map_input = read_map(filename)
    x = 0
    wrap_at = len(map_input[0])
    count = 0

    for line in with_first_element_skipped(map_input):
        x = (x + 3) % wrap_at
        if line[x] == TREE:
            count += 1
    return count


def with_first_element_skipped(a_list: List[str]) -> Iterable[str]:
    an_iterator = iter(a_list)
    next(an_iterator)
    return an_iterator
