from rucksack import item_priority
import pytest


@pytest.mark.parametrize(
    "item,priority",
    [
        ("A", 27),
        ("Z", 52),
        ("G", 33),
    ],
)
def test_item_priority(item, priority):
    assert item_priority(item) == priority
