import re
from collections import Counter
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Food:
    ingredients: List[str]
    allergens: List[str]


def part1(input_data: str) -> int:
    foods = read_foods(input_data)

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


def part2(input_data: str) -> str:
    foods = read_foods(input_data)

    candidates = {}
    for food in foods:
        for allergen in food.allergens:
            if allergen in candidates:
                candidates[allergen] &= set(food.ingredients)
            else:
                candidates[allergen] = set(food.ingredients)

    allergens = {}
    while candidates:
        # need to have a hard copy as the dict is going to be modified
        found = [allergen for allergen in candidates if len(candidates[allergen]) == 1]
        ingredients_to_remove = set()
        for allergen in found:
            (ingredient,) = candidates[allergen]
            allergens[allergen] = ingredient
            ingredients_to_remove.add(ingredient)
            del candidates[allergen]

        for ingredients in candidates.values():
            ingredients -= ingredients_to_remove

    return ",".join(allergens[allergen] for allergen in sorted(allergens))


line_parser = re.compile(r"([^(]+) \(contains ([^)]+)\)")


def read_foods(input_data: str) -> List[Food]:
    return [parse_food(line) for line in input_data.splitlines()]


def parse_food(line: str) -> Food:
    groups = line_parser.fullmatch(line).groups()
    return Food(groups[0].split(" "), groups[1].split(", "))
