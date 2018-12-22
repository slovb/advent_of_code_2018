def erosion_level((x, y), depth, start, target, mem):
    position = (x, y)
    # memoization
    if position in mem:
        return mem[position]
    # geological index
    if position == start:
        gi = 0
    elif position == target:
        gi = 0
    elif y == 0:
        gi = 16807 * x
    elif x == 0:
        gi = 48271 * y
    else:
        recurse = lambda x, y: erosion_level((x, y), depth, start, target, mem)
        gi = recurse(x-1, y) * recurse(x, y-1)
    # remember and output
    mem[position] = (depth + gi) % 20183
    return mem[position]

def render(depth, start, target, mem):
    def region(el):
        return '.=|'[el % 3]
    out = []
    for y in range(target[1] + 6):
        line = []
        for x in range(target[0] + 6):
            p = (x, y)
            if p == start:
                line.append('M')
                continue
            elif p == target:
                line.append('T')
                continue
            el = erosion_level(p, depth, start, target, mem)
            line.append(region(el))
        out.append(''.join(line))
    return '\n'.join(out)

def solve(depth, target):
    start = (0, 0)
    mem = {}
    risk = 0
    for y in range(target[1] + 1):
        for x in range(target[0] + 1):
            el = erosion_level((x, y), depth, start, target, mem)
            risk += (el % 3)
    #print render(depth, start, target, mem)
    return risk

if __name__ == '__main__':
    import sys
    int_arg = lambda k: int(sys.argv[k])
    depth = int_arg(1)
    target = (int_arg(2), int_arg(3))
    print solve(depth, target)
