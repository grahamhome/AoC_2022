import sys

p2_scores = {
    "A": {
        "X": 3 + 0,
        "Y": 1 + 3,
        "Z": 2 + 6,
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6,
    },
    "C": {
        "X": 2 + 0,
        "Y": 3 + 3,
        "Z": 1 + 6,
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
