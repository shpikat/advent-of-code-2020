from day21.common import read_foods


def solve(filename: str) -> str:
    foods = read_foods(filename)

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

    return ','.join(allergens[allergen] for allergen in sorted(allergens))
