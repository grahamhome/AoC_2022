import sys

from solutions.dec_03.rucksack import item_priority


def badge(rucksacks):
    return list(
        set(rucksacks[0])
        .intersection(set(rucksacks[1]))
        .intersection(set(rucksacks[2]))
    )[0]


def badges_sum(filepath):
    rucksacks = [rucksack.strip() for rucksack in open(filepath, "r").readlines()]
    group_list = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]
    return sum([item_priority(badge(group)) for group in group_list])


if __name__ == "__main__":
    print(badges_sum(sys.argv[1]))
