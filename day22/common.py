from collections import deque
from typing import List


def read_decks(filename: str) -> List[deque]:
    with open(filename, "r") as file:
        return [read_deck(deck) for deck in file.read().rstrip().split('\n\n')]


def read_deck(deck: str) -> deque:
    return deque(int(card) for card in deck.strip().split('\n')[1:])
