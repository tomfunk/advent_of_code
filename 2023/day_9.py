sample = [
    "0 3 6 9 12 15\n",
    "1 3 6 10 15 21\n",
    "10 13 16 21 30 45\n",
]


def get_delta(line):
    return [line[i + 1] - line[i] for i in range(len(line) - 1)]


def get_next(line):
    if set(line) == set([0]):
        return 0
    return line[-1] + get_next(get_delta(line))


def get_sum(lines):
    total = 0
    for line in lines:
        line = [int(i) for i in line.strip().split(' ')]
        total += get_next(line)
    return total


def get_prev(line):
    if set(line) == set([0]):
        return 0
    return line[0] - get_prev(get_delta(line))


def get_sum_prev(lines):
    total = 0
    for line in lines:
        line = [int(i) for i in line.strip().split(' ')]
        total += get_prev(line)
    return total


def main():
    print("sample 1a:", get_sum(sample))
    print("sample 2:", get_sum_prev(sample))

    with open("inputs/day_9.txt") as f:
        lines = f.readlines()
    print("part 1:", get_sum(lines))
    print("part 2:", get_sum_prev(lines))

if __name__ == "__main__":
    main()