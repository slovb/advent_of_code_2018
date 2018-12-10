def render(state):
    positions = [s['position'] for s in state]
    x_positions = [p[0] for p in positions]
    x_min = min(x_positions)
    x_max = max(x_positions)
    y_positions = [p[1] for p in positions]
    y_min = min(y_positions)
    y_max = max(y_positions)
    output = []
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) in positions:
                output.append('#')
            else:
                output.append('.')
        output.append('\n')
    return "".join(output)

def explore(state, time):
    for s in state:
        p = s['position'] 
        v = s['velocity']
        np = (p[0] + time*v[0], p[1] + time*v[1])
        s['position'] = np
    return render(state)

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

def main(filename, time):
    return explore(read(filename), time)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 3):
        print('missing input parameter')
        exit()
    print main(sys.argv[1], int(sys.argv[2]))

