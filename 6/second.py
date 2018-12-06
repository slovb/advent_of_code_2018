def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def lower_bound(coordinates):
    x = coordinates[0][0]
    y = coordinates[0][1]
    for c in coordinates:
        if c[0] < x:
            x = c[0]
        if c[1] < y:
            y = c[1]
    return (x, y)

def upper_bound(coordinates):
    x = coordinates[0][0]
    y = coordinates[0][1]
    for c in coordinates:
        if c[0] > x:
            x = c[0]
        if c[1] > y:
            y = c[1]
    return (x, y)

def solve(coordinates, limit):
    lb = lower_bound(coordinates)
    ub = upper_bound(coordinates)
    from sets import Set
    inside = Set()
    vis = []
    step = 1
    for y in range(lb[1] - step, ub[1] + step + 1):
        for x in range(lb[0] - step, ub[0] + step + 1):
            p = (x, y)
            d = [distance(p, c) for c in coordinates]
            if sum(d) < limit:
                inside.add(p)
                vis.append('#')
            else:
                vis.append('.')
        vis.append('\n')
    print "".join(vis)
    return len(inside)

def read(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        coordinates = []
        for l in lines:
            x = int(l.split(',')[0])
            y = int(l.split(' ')[1])
            coordinates.append((x, y)) 
        return coordinates

def main(filename):
    return solve(read(filename), 10000)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))

