import sys

from solutions.dec_08.height_checker import get_forest


def best_view(forest):
    best = 0
    for row_index in range(1, len(forest) - 1):
        for column_index in range(1, len(forest[0]) - 1):
            best = max(
                best,
                view_distance(
                    limit=forest[row_index][column_index],
                    scene=list(reversed(forest[row_index][:column_index])),
                )
                * view_distance(
                    limit=forest[row_index][column_index],
                    scene=forest[row_index][column_index + 1 :],
                )
                * view_distance(
                    limit=forest[row_index][column_index],
                    scene=list(
                        reversed([row[column_index] for row in forest[:row_index]])
                    ),
                )
                * view_distance(
                    limit=forest[row_index][column_index],
                    scene=[row[column_index] for row in forest[row_index + 1 :]],
                ),
            )
    return best


def view_distance(limit: int, scene: list) -> int:
    """
    Counts the items in scene LTR until limit is reached.
    """
    distance = 0
    while scene:
        distance += 1
        if scene[0] >= limit:
            break
        scene = scene[1:]

    return distance


if __name__ == "__main__":
    print(best_view(get_forest(sys.argv[1])))
