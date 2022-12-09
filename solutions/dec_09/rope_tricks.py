import re
import sys


def update_coords(coords, direction):
    """
    Updates the given coordinates to simulate an object moving 1 unit in the given direction
    :param coords: (int, int)
    :param direction: string, one of "U", "D", "L" or "R"
    :return: (int, int)
    """
    if direction == "U":
        return coords[0] + 1, coords[1]
    elif direction == "D":
        return coords[0] - 1, coords[1]
    elif direction == "R":
        return coords[0], coords[1] + 1
    elif direction == "L":
        return coords[0], coords[1] - 1
    else:
        raise ValueError


def objects_diagonal(coords_1, coords_2):
    """
    Determines whether two coordinate pairs
    are diagonal to each other.
    """
    return (abs(coords_1[0] - coords_2[0]), abs(coords_1[1] - coords_2[1])) == (1, 1)


def objects_neighbors(coords_1, coords_2):
    """
    Determines whether two coordinate pairs
    are next to each other.
    """
    return (coords_1[0] == coords_2[0] and abs(coords_1[1] - coords_2[1]) == 1) or (
        coords_1[1] == coords_2[1] and abs(coords_1[0] - coords_2[0]) == 1
    )


def objects_adjacent(coords_1, coords_2):
    return objects_diagonal(coords_1, coords_2) or objects_neighbors(coords_1, coords_2)


def objects_colinear(coords_1, coords_2):
    return coords_1[0] == coords_2[0] or coords_1[1] == coords_2[1]


def push_rope(moves):
    """
    Difficult and unsatisfying.
    """
    head = (0, 0)
    tail = (0, 0)
    tail_positions = [tail]

    for move in moves:
        direction, distance = re.search(
            pattern=r"^([UDLR]) ([0-9]+)$", string=move
        ).groups()
        for _ in range(int(distance)):
            head = update_coords(head, direction)
            if not head == tail:
                if not objects_adjacent(head, tail):
                    if not objects_colinear(head, tail):
                        # Special case: head drags tail
                        if direction in ("U", "D"):
                            # We are moving up or down, so tail must shift left or right
                            tail = (tail[0], head[1])
                        else:
                            # We are moving left or right, so tail must shift up or down
                            tail = (head[0], tail[1])
                    tail = update_coords(tail, direction)
                    tail_positions.append(tail)
    return tail_positions


def count_unique_positions(filepath):
    return len(
        set(
            push_rope([move.strip() for move in open("data/rope.txt", "r").readlines()])
        )
    )


if __name__ == "__main__":
    print(count_unique_positions(sys.argv[1]))
