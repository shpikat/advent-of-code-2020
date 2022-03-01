import re
from dataclasses import dataclass
from typing import List, Set, Tuple


def part1(input_data: str) -> int:
    rules, your_ticket, nearby_tickets = read_rules_and_tickets(input_data)

    error_rate = sum(
        field for ticket in nearby_tickets for field in ticket if is_field_invalid(rules, field)
    )
    return error_rate


def is_field_invalid(rules: List[Tuple[str, int, int, int, int]], field: int) -> bool:
    return not any(
        low1 <= field <= high1 or low2 <= field <= high2 for _, low1, high1, low2, high2 in rules
    )


@dataclass
class Node:
    name: str
    low: int
    high: int
    max: int = None
    left: "Node" = None
    right: "Node" = None


def part2(input_data: str) -> int:
    rules, your_ticket, nearby_tickets = read_rules_and_tickets(input_data)

    valid_tickets = [ticket for ticket in nearby_tickets if is_ticket_valid(rules, ticket)]

    """
    It's definitely way excessive for this task, but I so wanted to use it!
    """
    rules_tree = build_augmented_interval_tree(rules)

    candidates = [
        set.intersection(*(find_overlaps(rules_tree, value) for value in field_values))
        for field_values in zip(*valid_tickets)
    ]

    """
    We can speed things up by removing completely any fields that are not required for the result. 
    That will speed things up, but won't change the main algorithm. And the input data is really small for the task.
    """
    fields = [""] * len(candidates)
    next_found_field = None
    for _ in range(len(candidates) + 1):
        found_field = next_found_field
        for position, field in enumerate(candidates):
            field.discard(found_field)
            if len(field) == 1:
                (next_found_field,) = field
                fields[position] = next_found_field

    result = 1
    for position, name in enumerate(fields):
        if name.startswith("departure"):
            result *= your_ticket[position]
    return result


def is_ticket_valid(rules: List[Tuple[str, int, int, int, int]], ticket: List[int]) -> bool:
    return not any(is_field_invalid(rules, field) for field in ticket)


def build_augmented_interval_tree(values: List[Tuple[str, int, int, int, int]]) -> Node:
    root = None
    for name, low1, high1, low2, high2 in values:
        root = add(root, Node(name, low1, high1))
        root = add(root, Node(name, low2, high2))
    return root


def add(root: Node, node: Node) -> Node:
    if root:
        if node.low < root.low:
            root.left = add(root.left, node)
        else:
            root.right = add(root.right, node)
        if root.max < node.high:
            root.max = node.high
    else:
        node.max = node.high
        root = node
    return root


def find_overlaps(root: Node, value: int) -> Set[str]:
    overlaps = set()
    stack = []
    current = root
    while current or stack:
        if current:
            if current.max >= value:
                stack.append(current)
                current = current.left
            else:
                current = None
        else:
            current = stack.pop()
            if value < current.low:
                current = None
            else:
                if value <= current.high:
                    overlaps.add(current.name)
                current = current.right
    return overlaps


pattern = re.compile(r"^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)$")


def read_rules_and_tickets(
    input_data: str,
) -> Tuple[List[Tuple[str, int, int, int, int]], List[int], List[List[int]]]:
    sections = input_data.split("\n\n")
    return (
        get_rules(sections[0].splitlines()),
        get_your_ticket(sections[1].splitlines()),
        get_nearby_tickets(sections[2].splitlines()),
    )


def get_rules(lines: List[str]) -> List[Tuple[str, int, int, int, int]]:
    return [get_rule(line) for line in lines if line]


def get_rule(line: str) -> Tuple[str, int, int, int, int]:
    m = pattern.fullmatch(line)
    return (
        m.group(1),
        int(m.group(2)),
        int(m.group(3)),
        int(m.group(4)),
        int(m.group(5)),
    )


def get_your_ticket(lines: List[str]) -> List[int]:
    return get_ticket(lines[1])


def get_nearby_tickets(lines: List[str]) -> List[List[int]]:
    return [get_ticket(line) for line in lines[1:] if line]


def get_ticket(line: str) -> List[int]:
    return [int(number) for number in line.split(",")]
