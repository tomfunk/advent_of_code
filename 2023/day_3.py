numbers = set(list("1234567890"))
stop = ["."]

number_log = dict()
# {
#     0: {
#         "value": "4",
#         "line_index": 0
#         "char_indexes": []
#     }
# }

symbol_log = []
gear_log = []
# (i, j)

index_map = dict()
# {
#     0:{
#         0: {
#             "value": "4",
#             "type": "number"
#             "part_number": False
#             "number_log_index": 0
#         }
#     }
# }

def process_lines(lines):

    number_log_index = -1
    last_type_num = False
    for i, line in enumerate(lines):
        if i not in index_map:
            index_map[i] = dict()
        for j, char in enumerate(line.strip()):
            if char in numbers:
                curr_type = "number"
                if not last_type_num:
                    number_log_index += 1
                    number_log[number_log_index] = {
                        "value": "",
                        "line_index": i,
                        "char_indexes": [],
                        "part_number": False,
                    }

                # append to number_log entry
                number_log[number_log_index]["value"] += char
                number_log[number_log_index]["char_indexes"].append(j)
            elif char in stop:
                curr_type = "stop"
            else:
                curr_type = "symbol"
                for k in [i - 1, i, i + 1]:
                    for l in [j - 1, j, j + 1]:
                        if k >= 0 and l >= 0:
                            symbol_log.append((k, l))
            if char == "*":
                symbol_area = []
                for k in [i - 1, i, i + 1]:
                    for l in [j - 1, j, j + 1]:
                        if k >= 0 and l >= 0:
                            symbol_area.append((k, l))
                gear_log.append(symbol_area)
            
            index_map[i][j] = {
                "value": char,
                "type": curr_type,
                "part_number": False,
                "number_log_index": number_log_index if curr_type == "number" else None
            }

            if curr_type == "number":
                last_type_num = True
            else:
                last_type_num = False

def check_symbols():
    for (i, j) in symbol_log:
        if i in index_map and j in index_map[i]:
            index_map[i][j]["part_number"] = True
            number_log_index = index_map[i][j]["number_log_index"]
            if number_log_index is not None:
                number_log[number_log_index]["part_number"] = True


def check_gears():
    total = 0
    for symbol_area in gear_log:
        number_log_indexes = set()
        for (i, j) in symbol_area:
            if i in index_map and j in index_map[i]:
                number_log_index = index_map[i][j]["number_log_index"]
                if number_log_index is not None:
                    number_log_indexes.add(number_log_index)
        if len(number_log_indexes) == 2:
            number_values = [int(number_log[nli]["value"]) for nli in number_log_indexes]
            total += number_values[0] * number_values[1]
    return total


def sum_totals():
    total = 0
    not_parts_count = 0
    for number in number_log.values():
        if number["part_number"]:
            total += int(number["value"])
    return total


def both_parts(lines):
    process_lines(lines)
    check_symbols()    
    return sum_totals(), check_gears()

def main():
    lines = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]

    with open("inputs/day_3.txt") as f:
        lines = f.readlines()
    part_1, part_2 = both_parts(lines)
    print("part 1:", part_1)
    print("part 2:", part_2)


if __name__ == "__main__":
    main()