rl_map = {"L": 0, "R": 1}

sample = [
    "RL",
    "",
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)",
]

sample2 = [
    "LLR",
    "",
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",
]

sample3 = [
    "LR\n",
    "\n",
    "11A = (11B, XXX)\n",
    "11B = (XXX, 11Z)\n",
    "11Z = (11B, XXX)\n",
    "22A = (22B, XXX)\n",
    "22B = (22C, 22C)\n",
    "22C = (22Z, 22Z)\n",
    "22Z = (22B, 22B)\n",
    "XXX = (XXX, XXX)\n",
]

def get_nodes(lines):
    directions = lines[0].strip()
    nodes = dict()
    for line in lines[2:]:
        key, values = line.strip().split(" = ")
        values = values.strip('()').split(', ')
        nodes[key] = values
    return directions, nodes


def get_num_steps(lines):
    next_node = "AAA"
    steps = 0
    directions, nodes = get_nodes(lines)
    while next_node != "ZZZ":
        i = steps % len(directions)
        next_node = nodes[next_node][rl_map[directions[i]]]
        steps +=1
    return steps

def factor(n):
    for i in range(2, n//2):
        if n / i < i:
            break
        if n % i == 0:
            return [i] + factor(n//i)
    return [n]

def lcd(numbers):
    factors = set()
    for number in numbers:
        factors = factors.union(factor(number))
    output = 1
    for f in factors:
        output *= f
    return output

def get_num_ghost_steps(lines):
    steps = 0
    directions, nodes = get_nodes(lines)
    next_nodes = list(filter(lambda x: x[-1] == "A", nodes))
    node_z_indexes = [0 for _ in range(len(next_nodes))]
    while any(map(lambda x: x == 0, node_z_indexes)):
        i = steps % len(directions)
        next_nodes = [nodes[next_node][rl_map[directions[i]]] for next_node in next_nodes]
        steps +=1
        for j in range(len(node_z_indexes)):
            if next_nodes[j][-1] == "Z":
                node_z_indexes[j] = steps
        
    return lcd(node_z_indexes)


def main():
    print("sample 1a:", get_num_steps(sample))
    print("sample 1b:", get_num_steps(sample2))
    print("sample 2:", get_num_ghost_steps(sample3))

    with open("inputs/day_8.txt") as f:
        lines = f.readlines()
    print("part 1:", get_num_steps(lines))
    print("part 2:", get_num_ghost_steps(lines))

if __name__ == "__main__":
    main()