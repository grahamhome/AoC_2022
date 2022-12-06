import sys


def find_marker_index(filepath, marker_size):
    data = open(filepath, "r").readlines()[0].strip()
    index_low = 0
    index_high = marker_size
    window = data[index_low:index_high]
    while not len(set(window)) == marker_size:
        index_low += 1
        index_high += 1
        window = data[index_low:index_high]
    return index_high


if __name__ == "__main__":
    print(find_marker_index(sys.argv[1], int(sys.argv[2])))
