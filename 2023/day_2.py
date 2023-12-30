limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def check_game(line):
    game_id, records = line.split(':')
    game_id = int(game_id.split(" ")[1])
    records = records.split(";")
    for record in records:
        for color_pair in record.split(","):
            number, color = color_pair.strip().split(" ")
            number = int(number)
            if number > limits[color]:
                return 0
    return game_id


def get_power(line):
    game_id, records = line.split(':')
    game_id = int(game_id.split(" ")[1])
    records = records.split(";")
    max_colors = {}
    for record in records:
        for color_pair in record.split(","):
            number, color = color_pair.strip().split(" ")
            number = int(number)
            if number > max_colors.get(color, 0):
                max_colors[color] = number
    power = 1
    for v in max_colors.values():
        power *= v
    return power


def main():
    with open("inputs/day_2.txt") as f:
        # print("part 1:", sum([check_game(line) for line in f]))
        print("part 2:", sum([get_power(line) for line in f]))


if __name__ == "__main__":
    main()
