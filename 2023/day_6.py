sample = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]


def get_races(lines):
    times = (int(l) for l in lines[0].split(" ")[1:] if l != "")
    distances = (int(l) for l in lines[1].split(" ")[1:] if l != "")
    return list(zip(times, distances))


def get_race(lines):
    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))
    return time, distance


def get_distance(hold, time):
    return (time - hold) * hold


def get_record_breaker_counts(time, distance):
    i, j = 0, round(time / 2)
    while i < j:
        mid = (i + j) / 2
        mid_dist = get_distance(round(mid), time)
        if i == j - 1:
            break
        if mid_dist < distance:
            i = round(mid)
        elif mid_dist > distance:
            j = round(mid)
        else:
            break

    if time % 2 == 1:
        return int(time - 2 * mid)
    return int(time - 2 * mid)


def get_races_margin(lines):
    margin = 1
    for time, distance in get_races(lines):
        margin *= get_record_breaker_counts(time, distance)
    return margin

def get_race_margin(lines):
    time, distance = get_race(lines)
    return get_record_breaker_counts(time, distance)



def main():
    print("sample 1:", get_races_margin(sample))
    print("sample 2:", get_race_margin(sample))  # is this wrong?

    with open("inputs/day_6.txt") as f:
        lines = f.readlines()
    print("part 1:", get_races_margin(lines))
    print("part 2:", get_race_margin(lines))

if __name__ == "__main__":
    main()
