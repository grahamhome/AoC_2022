import sys


def find_marker_index(filepath, marker_size):
    data = open(filepath, "r").readlines()[0].strip()
    index = marker_size
    while not len(set(data[index - marker_size : index])) == marker_size:
        index += 1
    return index


if __name__ == "__main__":
    print(find_marker_index(sys.argv[1], int(sys.argv[2])))
