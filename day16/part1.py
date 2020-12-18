from typing import List, Tuple

from day16.common import read_rules_and_tickets


def main():
    rules, your_ticket, nearby_tickets = read_rules_and_tickets()

    error_rate = sum((field for ticket in nearby_tickets
                      for field in ticket
                      if is_field_invalid(rules, field)))
    print(error_rate)


def is_field_invalid(rules: List[Tuple[str, int, int, int, int]], field: int) -> bool:
    return not any(low1 <= field <= high1 or low2 <= field <= high2
                   for _, low1, high1, low2, high2 in rules)


if __name__ == "__main__":
    main()
