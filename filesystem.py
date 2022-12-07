import sys

import regex as re

cd_pattern = r"^\$ cd (\S+)$"
ls_pattern = r"^\$ ls$"
file_pattern = r"^(\d+) (\S+)$"
dir_pattern = r"^dir (\S+)$"


def filesystem(command_history):
    """
    Returns a dict representing the filesystem indicated by the given command history.
    """
    pwd = []
    fs: dict[str, dict | int] = {"/": {}}

    while command_history:
        command, history = command_history[0], command_history[1:]
        if cd_match := re.search(cd_pattern, command):
            dirname = cd_match.groups()[0]
            if dirname != "..":
                pwd.append(dirname)
            else:
                pwd.pop()
            command_history = history
        elif re.search(ls_pattern, command):
            index = 0
            curr_dir = fs
            for dir in pwd:
                curr_dir = curr_dir[dir]
            while index < len(history):
                if re.search(cd_pattern, history[index]) or re.search(
                    ls_pattern, history[index]
                ):
                    break
                if file_match := re.search(file_pattern, history[index]):
                    curr_dir[file_match.groups()[1]] = int(file_match.groups()[0])
                elif dir_match := re.search(dir_pattern, history[index]):
                    curr_dir[dir_match.groups()[0]] = {}
                index += 1
            command_history = history[index:]
    return fs


def size_at_path(filesystem):
    """Recursively computes the size of all files at a given path in a given filesystem."""
    return sum(
        item if isinstance(item, int) else size_at_path(item)
        for item in filesystem.values()
    )


def all_dir_sizes(filesystem):
    """
    Recurses into filesystem, calculating the size of each dict and adding it to a list.
    :param filesystem:
    :param sizes:
    :return:
    """
    sizes = [0]
    for item in filesystem.values():
        if isinstance(item, int):
            sizes[0] += item
        else:
            dir_sizes = all_dir_sizes(item)
            sizes[0] += dir_sizes[0]
            sizes += dir_sizes
    return sizes


def small_directories_sum(input_file_path):
    return sum(
        filter(
            lambda size: size <= 100_000,
            all_dir_sizes(
                filesystem(
                    [line.strip() for line in open(input_file_path, "r").readlines()]
                )
            ),
        )
    )


disk_size = 70000000
required_size = 30000000


def smallest_dir_to_delete(input_file_path):
    dir_sizes = all_dir_sizes(
        filesystem([line.strip() for line in open(input_file_path, "r").readlines()])
    )
    free_space = disk_size - max(dir_sizes)
    space_to_free = required_size - free_space
    print(space_to_free)
    for dir_size in sorted(dir_sizes):
        if dir_size >= space_to_free:
            return dir_size


if __name__ == "__main__":
    print(smallest_dir_to_delete(sys.argv[1]))
    # print(f"{small_directories_sum(sys.argv[1])}")
