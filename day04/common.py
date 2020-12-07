from typing import List, Dict


def read_input() -> List[Dict[str, str]]:
    with open("input", "r") as file:
        return [dict(entry.split(':') for entry in group.split())
                for group in file.read().split('\n\n')]
