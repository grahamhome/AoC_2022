import string
import sys


def item_priority(item):
    if item in string.ascii_lowercase:
        return 1 + ord(item) - ord("a")
    if item in string.ascii_uppercase:
        return 27 + ord(item) - ord("A")


def odd_item(rucksack):
    if len(rucksack) > 2:
        return list(
            set(rucksack[: len(rucksack) // 2]).intersection(
                set(rucksack[len(rucksack) // 2 :])
            )
        )[0]
    else:
        return list(set(rucksack[:1]).intersection(set(rucksack[1:])))[0]


def odd_item_sum(filepath):
    return sum(
        map(
            lambda rucksack: item_priority(odd_item(rucksack.strip())),
            open(filepath, "r").readlines(),
        )
    )


if __name__ == "__main__":
    print(odd_item_sum(sys.argv[1]))
