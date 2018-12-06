def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def closest(coordinates, position):
    best = None
    val = float('Inf')
    count = 0
    for c in coordinates:
        d = distance(c, position)
        if d < val:
            val = d
            best = c
            count = 1
        elif d == val:
            count += 1
    if count == 1:
        return best
    # if tied return None
    return None

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

def visualize(c, coordinates, p):
    if p in coordinates:
        return '*'
    if not c:
        return '.'
    i = coordinates.index(c)
    return str(unichr(ord('A') + i))

def solve(coordinates):
    lb = lower_bound(coordinates)
    ub = upper_bound(coordinates)
    # calculate the areas within the bounds
    # this method should work even if there are duplicate coordinates
    areas = {}
    vis = []
    step = 1
    for y in range(lb[1] - step, ub[1] + step + 1):
        for x in range(lb[0] - step, ub[0] + step + 1):
            c = closest(coordinates, (x, y))
            vis.append(visualize(c, coordinates, (x, y)))
            if not c:
                continue
            if not c in areas:
                areas[c] = 0
            areas[c] += 1
        vis.append("\n")
    print "".join(vis)
    # filter out the infinites by going on the outer rim
    step = 2
    for x in range(lb[0] - step, ub[0] + step + 1):
        cl = closest(coordinates, (x, lb[1] - step))
        cu = closest(coordinates, (x, ub[1] + step + 1))
        if cl in areas:
            del areas[cl]
        if cu in areas:
            del areas[cu]
    for y in range(lb[1] - step, ub[1] + step + 1):
        cl = closest(coordinates, (lb[0] - step, y))
        cu = closest(coordinates, (ub[0] + step, y + 1))
        if cl in areas:
            del areas[cl]
        if cu in areas:
            del areas[cu]
    return max(areas.values())

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
    return solve(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))

