from collections import Counter
from typing import List


def part1(input_data: str) -> int:
    ratings = read_joltage_ratings(input_data)
    ratings.sort()
    counter = Counter()
    # account for the first connection to the outlet
    counter[ratings[0]] += 1
    for difference in (ratings[i] - ratings[i - 1] for i in range(1, len(ratings))):
        counter[difference] += 1

    # device adapter is always 3 jolts higher
    return counter[1] * (counter[3] + 1)


def part2(input_data: str) -> int:
    ratings = read_joltage_ratings(input_data)

    ratings.sort()
    # append device joltage
    device = ratings[-1] + 3
    ratings.append(device)

    possibilities_per_rating = {0: 1}
    for r in ratings:
        for_one = possibilities_per_rating.get(r - 1, 0)
        for_two = possibilities_per_rating.get(r - 2, 0)
        for_three = possibilities_per_rating.get(r - 3, 0)
        possibilities_per_rating[r] = for_one + for_two + for_three

    return possibilities_per_rating[device]


def read_joltage_ratings(input_data: str) -> List[int]:
    return [int(line.rstrip()) for line in input_data.splitlines()]
