from day10.common import read_joltage_ratings


def solve(filename: str) -> int:
    ratings = read_joltage_ratings(filename)

    ratings.sort()
    # append device joltage
    device = ratings[-1] + 3
    ratings.append(device)

    possibilities_per_rating = {0: 1}
    for r in ratings:
        possibilities_per_rating[r] = possibilities_per_rating.get(r - 1, 0) + \
                                      possibilities_per_rating.get(r - 2, 0) + \
                                      possibilities_per_rating.get(r - 3, 0)

    return possibilities_per_rating[device]
