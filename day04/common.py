from typing import Dict, List


def read_input(filename: str) -> List[Dict[str, str]]:
    with open(filename, "r") as file:
        return [dict(entry.split(':') for entry in group.split())
                for group in file.read().split('\n\n')]
