def render(rows):
    return "\n".join(rows)

def simulate(rows):
    x_len = len(rows[0])
    y_len = len(rows)
    def count_adjacent(x, y):
        o = 0
        w = 0
        l = 0
        for j in range(max(0, y - 1), min(y + 2, y_len)):
            for i in range(max(0, x - 1), min(x + 2, x_len)):
                if i == x and j == y:
                    continue
                a = rows[j][i]
                if a == '.':
                    o += 1
                elif a == '|':
                    w += 1
                else:
                    l += 1
        return (o, w, l)
    updated = []
    for y, row in enumerate(rows):
        line = []
        for x, acre in enumerate(row):
            adjacent = count_adjacent(x, y)
            if acre == '.' and adjacent[1] >= 3:
                line.append('|')
            elif acre == '|' and adjacent[2] >= 3:
                line.append('#')
            elif acre == '#' and min(adjacent[1], adjacent[2]) < 1:
                line.append('.')
            else:
                line.append(acre)
        updated.append(''.join(line))
    return updated

def value(rows):
    wooded = sum([r.count('|') for r in rows])
    yards = sum([r.count('#') for r in rows])
    return wooded * yards

def solve(rows, steps):
    # expect 1000 235080
    memory = {}
    values = {}
    i = 0
    while i < steps:
        rows = simulate(rows)
        h = hash("".join(rows))
        if h not in memory:
            val = value(rows)
            memory[h] = (i, val)
            values[i] = val
        else:
            j, v = memory[h]
            cycle = i - j
            skips = (steps - i) / cycle
            print i, j, cycle, skips
            remainder = (steps - i - 1) - skips * cycle
            k = j + remainder
            return values[k]
        i += 1
    return value(rows)

def read(filename):
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]

def main(filename, steps = 10):
    rows = read(filename)
    return solve(rows, steps)

if __name__ == "__main__":
    import sys
    print main(sys.argv[1], int(sys.argv[2]))

