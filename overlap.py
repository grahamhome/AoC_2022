import sys


def range_2_set(drange):
    return set(range(int(drange.split("-")[0]), int(drange.split("-")[1]) + 1))


def total_overlap_count(filepath):
    count = 0
    for range_set in open(filepath).readlines():
        range1, range2 = range_set.strip().split(",")
        if range_2_set(range1).issubset(range_2_set(range2)) or range_2_set(
            range1
        ).issuperset(range_2_set(range2)):
            count += 1
    return count


def partial_overlap_count(filepath):
    count = 0
    for range_set in open(filepath).readlines():
        range1, range2 = range_set.strip().split(",")
        if range_2_set(range1).intersection(range_2_set(range2)):
            count += 1
    return count


if __name__ == "__main__":
    print(partial_overlap_count(sys.argv[1]))
