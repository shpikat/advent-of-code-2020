from typing import List, Iterable

from day03.common import read_map, TREE


def main():
    map_input = read_map()
    x = 0
    wrap_at = len(map_input[0])
    count = 0

    for line in with_first_element_skipped(map_input):
        x = (x + 3) % wrap_at
        if line[x] == TREE:
            count += 1
    print(count)


def with_first_element_skipped(a_list: List[str]) -> Iterable[str]:
    an_iterator = iter(a_list)
    next(an_iterator)
    return an_iterator


if __name__ == "__main__":
    main()
