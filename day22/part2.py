import itertools
from collections import deque
from operator import itemgetter
from typing import List

from day22.common import read_decks


def main():
    decks = read_decks()

    winner_index = play_game(decks)

    print(sum(card * (i + 1) for i, card in enumerate(reversed(decks[winner_index]))))


def play_game(decks: List[deque]) -> int:
    history = set()
    while all(decks):
        # one deck is enough for the snapshot
        snapshot = tuple(decks[0])
        if snapshot in history:
            # in this case player 1 always wins
            return 0
        history.add(snapshot)

        current_round = tuple(deck.popleft() for deck in decks)

        if all(len(deck) >= card for card, deck in zip(current_round, decks)):
            w = play_game([deque(itertools.islice(deck, 0, card)) for card, deck in zip(current_round, decks)])

            for card in current_round if w == 0 else reversed(current_round):
                decks[w].append(card)

        else:
            current_round_result = sorted(((card, deck) for card, deck in zip(current_round, decks)),
                                          key=itemgetter(0),
                                          reverse=True)
            _, round_winner = current_round_result[0]
            for card, _ in current_round_result:
                round_winner.append(card)
    return next(i for i, deck in enumerate(decks) if deck)


if __name__ == "__main__":
    main()
