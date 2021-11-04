def read_labeling(filename: str) -> str:
    with open(filename, "r") as file:
        return file.read().rstrip()
