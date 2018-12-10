def limits(positions):
    x, y = zip(*positions)
    return min(x), max(x), min(y), max(y)

def render(positions):
    x_min, x_max, y_min, y_max = limits(positions)
    output = []
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) in positions:
                output.append('#')
            else:
                output.append('.')
        output.append('\n')
    return "".join(output)

def area(positions):
    x_min, x_max, y_min, y_max = limits(positions)
    return (1 + x_max - x_min) * (1 + y_max - y_min)

def solve(state):
    smallest_positions = simulate(state, 0)
    smallest_area = area(smallest_positions)
    t = 1
    while True:
        p = simulate(state, t)
        a = area(p)
        if a < smallest_area:
            smallest_positions = p
            smallest_area = a
        else:
            break
        t += 1
    return render(smallest_positions), t - 1

def simulate(state, time):
    positions = []
    for s in state:
        p = s['position'] 
        v = s['velocity']
        positions.append((p[0] + time*v[0], p[1] + time*v[1]))
    return positions

def read(filename):
    with open(filename, 'r') as f:
        state = []
        import re
        for l in f.readlines():
            a = re.findall(r'-?\d+', l)
            state.append({
                'position': (int(a[0]), int(a[1])),
                'velocity': (int(a[2]), int(a[3])),
            })
        return state

def main(filename):
    return solve(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        pretty, time = main(f)
        print pretty
        print "\nElapsed time: {}".format(time)

