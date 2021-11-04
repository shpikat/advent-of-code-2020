from operator import itemgetter

from day22.common import read_decks


def solve(filename: str) -> int:
    decks = read_decks(filename)

    while all(decks):
        current_round = sorted(((deck.popleft(), deck) for deck in decks), key=itemgetter(0), reverse=True)
        _, round_winner = current_round[0]
        for card, _ in current_round:
            round_winner.append(card)

    winner = next(deck for deck in decks if deck)
    return sum(card * (i + 1) for i, card in enumerate(reversed(winner)))
