from collections import Counter

from day21.common import read_foods


def main():
    foods = read_foods()

    counts = Counter()
    candidates = {}
    for food in foods:
        counts.update(food.ingredients)
        for allergen in food.allergens:
            if allergen in candidates:
                candidates[allergen] &= set(food.ingredients)
            else:
                candidates[allergen] = set(food.ingredients)

    for ingredients in candidates.values():
        for ingredient in ingredients:
            del counts[ingredient]

    # or counts.total() since Python 3.10
    print(sum(count for _, count in counts.items()))


if __name__ == "__main__":
    main()
