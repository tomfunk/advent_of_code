num_strs = set("1234567890")
spelled_nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first_digit(line):
    for i in line:
        if i in num_strs:
            return i


def get_last_digit(line):
    for i in line[::-1]:
        if i in num_strs:
            return i


def get_first_digit_spelled(line):
    len_line = len(line)
    for i in range(len_line):
        if line[i] in num_strs:
            return line[i]
        for num_len in [3, 4, 5]:
            end_k = i + num_len
            if end_k < len_line and line[i:end_k] in spelled_nums:
                return spelled_nums[line[i:end_k]]


def get_last_digit_spelled(line):
    len_line = len(line)
    for i in range(len_line - 1, -1, -1):
        if line[i] in num_strs:
            return line[i]
        for num_len in [3, 4, 5]:
            start_k = i - num_len + 1
            if start_k > 0 and line[start_k:i + 1] in spelled_nums:
                return spelled_nums[line[start_k:i + 1]]


def get_value(line):
    return int(get_first_digit(line) + get_last_digit(line))


def get_value_spelled(line):
    return int(get_first_digit_spelled(line) + get_last_digit_spelled(line))


def main():
    with open("inputs/day_1.txt") as f:
        # print("part 1:", sum([get_value(line) for line in f]))
        print("part 2:", sum([get_value_spelled(line) for line in f]))


if __name__ == "__main__":
    main()
