import sys

import regex as re


def get_stacks(lines):
    lines, crate_names = lines[:-1], lines[-1].strip()
    crate_indices = [crate_names.index(name) + 1 for name in crate_names if name != " "]
    last_index = int(crate_names.split("   ")[-1])
    stacks = [[] for _ in range(last_index)]
    for line in lines:
        crate_contents = [line[index] for index in crate_indices]
        for index, content in enumerate(crate_contents):
            if content != " ":
                stacks[index].insert(0, content)
    return stacks


def apply_moves(moves, stacks, preserve_order=False):
    for move in moves:
        count, from_stack, to_stack = map(
            int,
            re.search(
                "move[[:space:]]([[:digit:]]+)[[:space:]]from[[:space:]]([[:digit:]]+)[[:space:]]to[[:space:]]([[:digit:]]+)\n",
                move,
            ).groups(),
        )
        if preserve_order:
            stacks[to_stack - 1] += stacks[from_stack - 1][-count:]
            stacks[from_stack - 1] = stacks[from_stack - 1][:-count]
        else:
            for _ in range(count):
                stacks[to_stack - 1].append(stacks[from_stack - 1].pop())
    return stacks


def get_stack_tops(stacks):
    return "".join(stack.pop() for stack in stacks)


def move_stacks(filepath, preserve_order):
    stack_data = open(filepath, "r").readlines()
    stacks = get_stacks(stack_data[: stack_data.index("\n")])
    moves = stack_data[stack_data.index("\n") + 1 :]
    stacks = apply_moves(moves, stacks, preserve_order=preserve_order)
    return get_stack_tops(stacks)


if __name__ == "__main__":
    print(move_stacks(sys.argv[1], bool(sys.argv[2])))
