import pytest

from solutions.dec_08.height_checker import count_visible_trees


@pytest.mark.parametrize(
    "forest,visible", [([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 3 * 4 - 4)]
)
def test_visible_trees(forest, visible):
    assert count_visible_trees(forest) == visible
