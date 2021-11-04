from dataclasses import dataclass
from typing import List, Set, Tuple

from day16.common import read_rules_and_tickets
from day16.part1 import is_field_invalid


@dataclass
class Node:
    name: str
    low: int
    high: int
    max: int = None
    left: 'Node' = None
    right: 'Node' = None


def solve(filename: str) -> int:
    rules, your_ticket, nearby_tickets = read_rules_and_tickets(filename)

    valid_tickets = [ticket for ticket in nearby_tickets if is_ticket_valid(rules, ticket)]

    '''
    It's definitely way excessive for this task, but I so wanted to use it!
    '''
    rules_tree = build_augmented_interval_tree(rules)

    candidates = [set.intersection(*(find_overlaps(rules_tree, value)
                                     for value in field_values))
                  for field_values in zip(*valid_tickets)]

    '''
    We can speed things up by removing completely any fields that are not required for the result. 
    That will speed things up, but won't change the main algorithm. And the input data is really small for the task.
    '''
    fields = [''] * len(candidates)
    next_found_field = None
    for _ in range(len(candidates) + 1):
        found_field = next_found_field
        for position, field in enumerate(candidates):
            field.discard(found_field)
            if len(field) == 1:
                next_found_field, = field
                fields[position] = next_found_field

    result = 1
    for position, name in enumerate(fields):
        if name.startswith('departure'):
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
