from collections import Counter

from day10.common import read_joltage_ratings


def main():
    ratings = read_joltage_ratings()
    ratings.sort()
    counter = Counter()
    # account for the first connection to the outlet
    counter[ratings[0]] += 1
    for difference in (ratings[i] - ratings[i - 1] for i in range(1, len(ratings))):
        counter[difference] += 1

    # device adapter is always 3 jolts higher
    print(counter[1] * (counter[3] + 1))


if __name__ == "__main__":
    main()
