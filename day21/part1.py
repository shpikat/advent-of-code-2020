from collections import Counter

from day21.common import read_foods


def solve(filename: str) -> int:
    foods = read_foods(filename)

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
    return sum(count for _, count in counts.items())
