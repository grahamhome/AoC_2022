import sys


def richest_elf(filepath):
    max_cals = 0
    current = 0
    for item in map(lambda i: i.strip(), open(filepath).readlines()):
        if item != "":
            current += int(item)
        else:
            max_cals = max(max_cals, current)
            current = 0
    return max(max_cals, current)


print(richest_elf(sys.argv[1]))
