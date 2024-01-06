sample = [
    "seeds: 79 14 55 13",
    "",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]

def get_seeds(line):
    return line.split(":")[1].strip().split(" ")


def parse_lines(lines):
    seeds = get_seeds(lines[0])
    maps = {}
    current_map = ""
    for line in lines[1:]:
        line = line.strip()
        if line == "":
            continue
        if line[-4:] == "map:":
            current_map = line[:-5]
            maps[current_map] = list()
            continue
        dest_start, source_start, n = line.split(" ")
        source_start, dest_start, n = int(source_start), int(dest_start), int(n)
        
        maps[current_map].append({
            "source_start": source_start,
            "source_end": source_start + n,
            "adjustment": dest_start - source_start,
            "dest_start": dest_start,
            "dest_end": dest_start + n,
        })

    return seeds, maps


def get_map_output(value, value_maps):
    for value_map in value_maps:
        if value >= value_map["source_start"] and value < value_map["source_end"]:
            return value + value_map["adjustment"]
    return value


def get_single_lookup(seed, maps):
    single_lookup = dict()
    value = get_map_output(seed, maps["seed-to-soil"])
    single_lookup["soil"] = value
    value = get_map_output(value, maps["soil-to-fertilizer"])
    single_lookup["fertilizer"] = value
    value = get_map_output(value, maps["fertilizer-to-water"])
    single_lookup["water"] = value
    value = get_map_output(value, maps["water-to-light"])
    single_lookup["light"] = value
    value = get_map_output(value, maps["light-to-temperature"])
    single_lookup["temperature"] = value
    value = get_map_output(value, maps["temperature-to-humidity"])
    single_lookup["humidity"] = value
    value = get_map_output(value, maps["humidity-to-location"])
    single_lookup["location"] = value
    return single_lookup


def get_lookup(lines):
    seeds, maps = parse_lines(lines)
    seed_lookup = dict()
    for seed in seeds:
        seed = int(seed)
        seed_lookup[seed] = get_single_lookup(seed, maps)
    return seed_lookup


def get_min_location(lines):
    lookup = get_lookup(lines)
    return min((d["location"] for d in lookup.values()))


def split_range(source_range, mapper):
    lower, upper = source_range
    split_points = [get_map_output(lower, mapper), get_map_output(upper, mapper)]
    # split_points = [lower, upper]
    for entry in mapper:
        if lower < entry["source_start"] and upper >= entry["source_start"]:
            # print(lower, "--->", entry["source_start"], "--->", upper)
            split_value = get_map_output(entry["source_start"], mapper)
            # split_value = entry["source_start"]
            split_points += [split_value, split_value + 1]
        if lower <= entry["source_end"] and upper > entry["source_end"]:
            # print(lower, "--->", entry["source_end"], "--->", upper)
            # split_value = entry["source_end"]
            split_value = get_map_output(entry["source_end"], mapper)
            split_points += [split_value, split_value + 1]
            
    split_points = sorted(list(set(split_points)))
    return [(split_points[i], split_points[i + 1]) for i in range(0,
    len(split_points), 2)]


def get_range_lookup(lines):
    seeds, maps = parse_lines(lines)

    ranges = [(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])) for i in range(0, len(seeds), 2)]
    map_names = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]    
    print("seeds")
    print(ranges)
    for map_name in map_names:
        new_ranges = []
        # split ranges
        for r in ranges:
            new_ranges += split_range(r, maps[map_name])
            # ranges = [(get_map_output(p[0], mapper), get_map_output(p[1], mapper)) for p in split_points])
            # print('before', ranges)
            # print('after', [(get_map_output(p[0], mapper), get_map_output(p[1], mapper)) for p in split_points])
        ranges = sorted(new_ranges)
        print(map_name)
        print(ranges)

def main():
    print("sample 1:", get_min_location(sample))
    print("sample 2:", get_range_lookup(sample))

    with open("inputs/day_5.txt") as f:
        lines = f.readlines()
    print("part 1:", get_min_location(lines))


if __name__ == "__main__":
    main()