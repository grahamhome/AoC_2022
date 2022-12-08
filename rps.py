import sys

p2_scores = {
    "A": {
        "X": 1 + 3,
        "Y": 2 + 6,
        "Z": 3 + 0,
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6,
    },
    "C": {
        "X": 1 + 6,
        "Y": 2 + 0,
        "Z": 3 + 3,
    },
}


def score_from_strategy(filepath):
    total = 0
    for p1_move, p2_move in map(
        lambda move: move.strip().split(" "), open(filepath, "r").readlines()
    ):
        total += p2_scores[p1_move][p2_move]
    return total


if __name__ == "__main__":
    print(score_from_strategy(sys.argv[1]))
