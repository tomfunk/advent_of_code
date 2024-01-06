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
            "range_start": source_start,
            "range_end": source_start + n,
            "adjustment": dest_start - source_start,
        })

    return seeds, maps

def get_map_output(value, value_maps):
    for value_map in value_maps:
        if value >= value_map["range_start"] and value < value_map["range_end"]:
            return value + value_map["adjustment"]
    return value


def get_lookup(lines):
    seeds, maps = parse_lines(lines)
    seed_lookup = dict()
    for seed in seeds:
        seed = int(seed)
        seed_lookup[seed] = dict()
        value = get_map_output(seed, maps["seed-to-soil"])
        seed_lookup[seed]["soil"] = value
        value = get_map_output(value, maps["soil-to-fertilizer"])
        seed_lookup[seed]["fertilizer"] = value
        value = get_map_output(value, maps["fertilizer-to-water"])
        seed_lookup[seed]["water"] = value
        value = get_map_output(value, maps["water-to-light"])
        seed_lookup[seed]["light"] = value
        value = get_map_output(value, maps["light-to-temperature"])
        seed_lookup[seed]["temperature"] = value
        value = get_map_output(value, maps["temperature-to-humidity"])
        seed_lookup[seed]["humidity"] = value
        value = get_map_output(value, maps["humidity-to-location"])
        seed_lookup[seed]["location"] = value
    return seed_lookup

def get_min_location(lines):
    lookup = get_lookup(lines)
    return min((d["location"] for d in lookup.values()))
    # return sorted(lookup.items(), key=lambda x: x[1]['location'])[0][0]

def main():
    print("sample 1:", get_min_location(sample))

    with open("inputs/day_5.txt") as f:
        lines = f.readlines()
    print("part 1:", get_min_location(lines))


if __name__ == "__main__":
    main()