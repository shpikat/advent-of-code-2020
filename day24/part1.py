from day24.common import read_instructions

moves = {
    'e': lambda x, y: (x + 1, y),
    'se': lambda x, y: (x, y - 1),
    'sw': lambda x, y: (x - 1, y - 1),
    'w': lambda x, y: (x - 1, y),
    'nw': lambda x, y: (x, y + 1),
    'ne': lambda x, y: (x + 1, y + 1),
}


def main():
    instructions = read_instructions()

    black_tiles = set()
    for line in instructions:
        tile = (0, 0)
        for instruction in line:
            tile = moves[instruction](*tile)
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)
    print(len(black_tiles))


if __name__ == "__main__":
    main()
