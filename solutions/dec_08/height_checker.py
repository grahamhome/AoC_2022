import sys


def count_visible_trees(forest):
    visible_trees = len(forest) * 4 - 4
    for row_index in range(1, len(forest) - 1):
        for column_index in range(1, len(forest[0]) - 1):
            if (
                forest[row_index][column_index]
                > max(forest[row_index][column_index + 1 :])
                or forest[row_index][column_index]
                > max(forest[row_index][:column_index])
                or forest[row_index][column_index]
                > max(row[column_index] for row in forest[row_index + 1 :])
                or forest[row_index][column_index]
                > max(row[column_index] for row in forest[:row_index])
            ):
                visible_trees += 1
    return visible_trees


def get_forest(filepath):
    return [
        [int(tree) for tree in row.strip()] for row in open(filepath, "r").readlines()
    ]


if __name__ == "__main__":
    print(count_visible_trees(get_forest(sys.argv[1])))
