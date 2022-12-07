import pytest

from filesystem import *


@pytest.mark.parametrize(
    "commands,expected_filesystem",
    [
        # (["$ cd /", "$ ls"], {"/": {}}),
        # (["$ cd /", "$ ls", "123 some_file.txt"], {"/": {"some_file.txt": 123}}),
        # (
        #     ["$ cd /", "$ ls", "dir abc", "$ cd abc", "$ ls", "123 some_file.txt"],
        #     {"/": {"abc": {"some_file.txt": 123}}},
        # ),
        (
            [
                "$ cd /",
                "$ ls",
                "dir abc",
                "dir def",
                "$ cd abc",
                "$ ls",
                "123 some_file.txt",
                "$ cd ..",
                "$ cd def",
                "$ ls",
                "456 other_file.txt",
            ],
            {"/": {"abc": {"some_file.txt": 123}, "def": {"other_file.txt": 456}}},
        ),
    ],
)
def test_filesystem(commands, expected_filesystem):
    assert filesystem(commands) == expected_filesystem


@pytest.mark.parametrize(
    "filesystem,expected_size",
    [
        ({}, 0),
        ({"dir_1": {}}, 0),
        ({"dir_1": {"file_1": 1}}, 1),
        ({"dir_1": {"file_1": 1}, "dir_2": {"file_1": 1, "file_2": 1}}, 3),
    ],
)
def test_size_at_path(filesystem, expected_size):
    assert size_at_path(filesystem) == expected_size


@pytest.mark.parametrize(
    "filesystem,expected_sizes",
    [
        ({}, [0]),
        ({"dir_1": {}}, [0, 0]),
        ({"dir_1": {"file_1": 1}}, [1, 1]),
        ({"dir_1": {"file_1": 1}, "dir_2": {"file_1": 1, "file_2": 1}}, [3, 1, 2]),
        (
            {"dir_1": {"file_1": 1}, "dir_2": {"file_1": 1, "dir_3": {"file_2": 1}}},
            [3, 1, 2, 1],
        ),
    ],
)
def test_all_dir_sizes(filesystem, expected_sizes):
    assert all_dir_sizes(filesystem) == expected_sizes
