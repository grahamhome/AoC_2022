def filesystem(command_history):
    """
    Returns a dict representing the filesystem indicated by the given command history.
    """
    cd_pattern = r"^\$ cd (\S+)$"
    ls_pattern = r"^\$ ls$"
    file_pattern = r"^(\d+) (\S+)$"
    dir_pattern = r"^dir (\S+)$"
    current_path = []
    filesystem = {
        "/": {}
    }  # TODO derive name from initial CD command (use CD match regex)
    index = 0
    # while index < len(current_path)
    # Command history only visits dirs after they are discovered, so no need for defaultdict.
    # Ignore the initial command for now, just create / directory
    # Check command_history[index] for LS or CD (regex match)
    # LS:
    # # Get dict representing current level of fs
    # - for dir in path:
    #       curr_dir = filesystem[dir]  <-- Is this where I would use a mutable borrow in Rust?
    # # get paths from LS
    #   new_paths = []
    #   index += 1
    #   while not command_history[index].startswith("$") and len(command_history[index:] > 0)
    #   new_paths.append(command_history[index])
    # # Add new paths to internal representation
    # for path in new_paths:
    #     if path matches file regex:
    #         add file as name: size to current directory
    #     elif path matches dir regex:
    #         add dir as name: {} to current directory
    # CD: Add dirname to current_path if not ..
    #     if .. then pop dirname from current_path


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
            lambda size: size <= 10_000,
            all_dir_sizes(
                filesystem(
                    line.strip() for line in open(input_file_path, "r").readlines()
                )
            ),
        )
    )
