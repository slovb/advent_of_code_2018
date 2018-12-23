def distance(u, v):
    return sum([abs(u[i]-v[i]) for i in range(len(u))])

def num_in_range(position, bots):
    in_range = lambda bot: distance(bot[0], position) <= bot[1]
    return len(filter(in_range, bots))

def remainder(position, bots):
    remaining = lambda bot: max(0, distance(bot[0], position) - bot[1])
    return sum(map(remaining, bots))

def deviate(p, d):
    out = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i != j or j != k:
                    out.append((p[0]+d*i, p[1]+d*j, p[2]+d*k))
    return out

def find_initial(bots):
    def getter(i):
        return lambda bot: bot[0][i]
    x = sum(map(getter(0), bots))/len(bots)
    y = sum(map(getter(1), bots))/len(bots)
    z = sum(map(getter(2), bots))/len(bots)
    return (x, y, z)

def improve_position(position, bots, banned):
    # find best point inside current cover
    queue = [position]
    start = (0,0,0)
    n = num_in_range(position, bots)
    d = distance(start, position)
    from sets import Set
    explored = Set()
    explored.add(position)
    for b in banned:
        explored.add(b)
    while len(queue) > 0:
        c = queue.pop()
        c_n = num_in_range(c, bots)
        if c_n < n:
            continue
        c_d = distance(start, c)
        if c_d > d:
            continue
        elif c_d < d:
            position = c
            d = c_d
            #print position, n, d
        candidates = deviate(position, 1)
        for c in candidates:
            if c not in explored:
                explored.add(c)
                queue.append(c)
    return position

def find_cover_position(position, bots, banned):
    def evaluate(p):
        return num_in_range(p, bots), remainder(p, bots)
    # find cover
    n = num_in_range(position, bots)
    r = remainder(position, bots)
    from sets import Set
    tried = Set()
    tried.add(position)
    for b in banned:
        tried.add(b)
    sl = 10**8 #step length
    while True:
        #print position, n, r
        candidates = deviate(position, sl)
        candidates = filter(lambda p: p not in tried, candidates)
        for c in candidates:
            tried.add(c)
        if len(candidates) == 0:
            if sl == 1:
                break
            sl /= 2
            continue
        updated = False
        for c in candidates:
            c_n, c_r = evaluate(c)
            if c_n > n or (c_n == n and c_r < r):
                updated = True
                n = c_n
                r = c_r
                position = c
        if not updated:
            if sl == 1:
                break
            sl /= 10
            continue
    return position

def solve(bots):
    solutions = []
    best_n = 0
    best_d = 0
    for i in range(1000):
        position = (0, 0, 0)
        position = find_initial(bots)
        position = find_cover_position(position, bots, solutions)
        position = improve_position(position, bots, solutions)
        n = num_in_range(position, bots)
        d = distance((0,0,0), position)
        if n > best_n or (n == best_n and d < best_d):
            best_n = n
            best_d = d
            print '!', n, d, position
        else:
            print '?', n, d, position
        solutions.append(position)
    return best_n, best_d

def read(filename):
    import re
    extract = lambda l: map(int, re.findall(r'-?\d+', l))
    with open(filename, 'r') as f:
        lines = map(extract, f.readlines())
        return [(tuple(l[:3]), l[3]) for l in lines]

def main(filename):
    bots = read(filename)
    return solve(bots)

if __name__ == "__main__":
    import sys
    print main(sys.argv[1])

