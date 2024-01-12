def get_step_direction(src, dest):
    i, j = dest
    m, n = src
    if i == m and j == n - 1:
        return "left"
    elif i == m and j == n + 1:
        return "right"
    elif i == m + 1 and j == n:
        return "down"
    elif i == m - 1 and j == n:
        return "up"
    return "invalid"

def validate_step(src, dest, lines):
    i, j = dest
    m, n = src
    next_pipe = lines[i][j] 
    sd = get_step_direction(src, dest)
    if next_pipe == "|" and sd in ["up", "down"]:
        return (i + i - m, j)
    elif next_pipe == "-" and sd in ["left", "right"]:
        return (i, j + j - n)
    elif next_pipe == "L" and sd == "left":
        return (i - 1, j)
    elif next_pipe == "L" and sd == "down":
        return (i, j + 1)
    elif next_pipe == "J" and sd == "right":
        return (i - 1, j)
    elif next_pipe == "J" and sd == "down":
        return (i, j - 1)
    elif next_pipe == "7" and sd == "right":
        return (i + 1, j)
    elif next_pipe == "7" and sd == "up":
        return (i, j - 1)
    elif next_pipe == "F" and sd == "left":
        return (i + 1, j)
    elif next_pipe == "F" and sd == "up":
        return (i, j + 1)
    return "error"

def find_start(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                return i, j


def get_srcs_dests(lines):
    start = find_start(lines)
    dests = [
        (start[0], start[1] - 1),
        (start[0], start[1] + 1),
        (start[0] - 1, start[1]),
        (start[0] + 1, start[1]),
    ]
    dests = list(filter(lambda x: x[0] >= 0 and x[1] >= 0 and validate_step(start, x, lines) != "error", dests))
    srcs = [start for _ in range(len(dests))]
    return srcs, dests


def get_empty_log(lines):
    log = []
    for line in lines:
        log_line = []
        for l in line.strip():
            log_line.append(".")
        log.append(log_line)
    return log


def follow_pipes(lines):
    srcs, dests = get_srcs_dests(lines)
    log = get_empty_log(lines)
    i = 1
    while dests[0] != dests[1]:
        i +=1
        for j in range(len(dests)):
            # print(i, srcs, dests)
            src = srcs[j]
            dest = dests[j]
            log[dest[0]][dest[1]] = lines[dest[0]][dest[1]]
            next_dest = validate_step(src, dest, lines)
            # print(next_dest)
            srcs[j] = dest
            dests[j] = next_dest
    return i #, log

def main():
    # print("sample 1:", follow_pipes(sample))
    # print("sample 2:", get_sum_prev(sample))

    with open("inputs/day_10.txt") as f:
        lines = f.readlines()
    print("part 1:", follow_pipes(lines))

if __name__ == "__main__":
    main()