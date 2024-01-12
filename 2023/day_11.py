sample = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#.....",
]


def rotate(lines, times=1):
    for _ in range(times):
        output = [list() for _ in range(len(lines[0]))]
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                output[j].insert(0, lines[i][j])
        lines = output
    return lines


def expand_flex(lines):
    lat = []
    long = []
    lines = rotate(lines)
    output = []
    for i in range(len(lines)):
        line = lines[i]
        if set(line) == set("."):
            output.append(["*" for _ in line])
            long.append(i)
        else:
            output.append(line)
    lines = rotate(output, 3)
    output = []
    for i in range(len(lines)):
        line = lines[i]
        if set(line) == set(".") or set(line) == set([".", "*"]):
            output.append(["*" for _ in line])
            lat.append(i)
        else:
            output.append(line)
    return output, lat, long


def get_galaxies_flex(lines):
    lines, lat, long = expand_flex(lines)
    galaxies = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                galaxies.append((i,j))
    return galaxies, lat, long


def get_counts(src, dest, lat, long):
    lat_long_count = 0
    for l in long:
        if (src[1] > l and l > dest[1]) or (src[1] < l and l < dest[1]):
            lat_long_count += 1
    for l in lat:
        if (src[0] > l and l > dest[0]) or (src[0] < l and l < dest[0]):
            lat_long_count += 1
    return lat_long_count


def get_path_dist(lines, mult=1):
    lines = [[l for l in s.strip()] for s in lines]
    
    galaxies, lat, long = get_galaxies_flex(lines)
    
    path_dist = 0
    pairs = 0
    for i, src in enumerate(galaxies[:-1]):
        for dest in galaxies[i+1:]:
            lat_long_count = get_counts(src, dest, lat, long)
            path_dist += abs(src[0] - dest[0]) + abs(src[1] - dest[1]) + lat_long_count * mult
            pairs += 1
    return path_dist

def main():
    print("sample 1:", get_path_dist(sample))
    print("sample 2a:", get_path_dist(sample, 9))
    print("sample 2b:", get_path_dist(sample, 99))

    with open("inputs/day_11.txt") as f:
        lines = f.readlines()
    print("part 1:", get_path_dist(lines))
    print("part 2:", get_path_dist(lines, 999999))

if __name__ == "__main__":
    main()