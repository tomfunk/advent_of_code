def split_line(line):
    line = line.split(":")[1].replace("  ", " ")
    winning_numbers, numbers = line.split("|")
    winning_numbers = set(winning_numbers.strip().split(" "))
    numbers = set(numbers.strip().split(" "))
    return winning_numbers, numbers


def score_line(line):
    winning_numbers, numbers = split_line(line)
    n_matches = len(winning_numbers.intersection(numbers))
    if n_matches == 0:
        return 0
    return 2 ** (n_matches - 1)


def recursive_score_line(i, lines, totals):
    line = lines[i]
    winning_numbers, numbers = split_line(line)
    n_matches = len(winning_numbers.intersection(numbers))
    score = 1
    for j in range(n_matches):
        if j + i + 1 not in totals:
            totals[j + i + 1] = recursive_score_line(j + i + 1, lines, totals)
        score += totals[j + i + 1]
    
    return score


def recursive_score_lines(lines):
    total = 0
    totals = dict()
    for i in range(len(lines)):
        totals[i] = recursive_score_line(i, lines, totals)
        total += totals[i]
    return total

def main():
    lines = [    
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]

    print("sample 1:", sum([score_line(line) for line in lines]))
    print("sample 2:", recursive_score_lines(lines))

    with open("inputs/day_4.txt") as f:
        lines = f.readlines()

    print("part 1:", sum([score_line(line) for line in lines]))
    print("part 2:", recursive_score_lines(lines))

if __name__ == "__main__":
    main()