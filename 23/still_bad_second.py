def distance(u, v):
    return abs(u[0]-v[0])+abs(u[1]-v[1])+abs(u[2]-v[2])

class Node():
    def __init__(self, p, r):
        self.p = p
        self.r = r
        self.connected = []

    def __repr__(self):
        return "{} {} {} {}".format( \
            self.p, \
            self.r, \
            len(self.connected), \
            self.distance((0,0,0)))

    def add(self, node):
        if self.close(node):
            self.connected.append(node)

    def close(self, node):
        # true if there exist a point that is in self and node
        # < will be correct because the point is within both
        return self.distance(node.p) < self.r + node.r
    
    def deviate(self, dx, dy, dz):
        return (self.p[0]+dx, self.p[1]+dy, self.p[2]+dz)

    def distance(self, u):
        return distance(u, self.p)

    def subdivide(self):
        nodes = []
        r = self.r / 2
        nodes.append(Node(self.deviate(-r, 0, 0), r))
        nodes.append(Node(self.deviate( r, 0, 0), r))
        nodes.append(Node(self.deviate( 0,-r, 0), r))
        nodes.append(Node(self.deviate( 0, r, 0), r))
        nodes.append(Node(self.deviate( 0, 0,-r), r))
        nodes.append(Node(self.deviate( 0, 0, r), r))
        for node in nodes:
            for c in self.connected:
                node.add(c)
        return nodes

def find_bound_range(bots):
    best_d = 0
    start = (0,0,0)
    for bot in bots:
        d = bot.distance(start) + bot.r
        if d > best_d:
            best_d = d
    l = 1
    while l < best_d:
        l *= 4 # My subdivision will divide by 4, this makes it safer?
    return l

def solve(bots):
    # start with a bound node, the subdivide and keep best
    start = (0,0,0)
    r = find_bound_range(bots)
    bound = Node(start, r)
    for bot in bots:
        bound.add(bot)
    queue = [bound]
    while r > 1:
        l = 0
        q = []
        for node in queue:
            parts = node.subdivide()
            for part in parts:
                l = max(l, len(part.connected))
                q.append(part)
        queue = filter(lambda node: len(node.connected) >= l, q)
        r = queue[0].r
        print r, len(queue), l
    dist = lambda node: node.distance(start)
    best = min(queue, key=dist)
    print best
    return best.distance(start)

def read(filename):
    import re
    extract = lambda l: map(int, re.findall(r'-?\d+', l))
    with open(filename, 'r') as f:
        lines = map(extract, f.readlines())
        bots = []
        for bot in [(tuple(l[:3]), l[3]) for l in lines]:
            p = bot[0]
            r = bot[1]
            bots.append(Node(p, r))
        return bots

def main(filename):
    bots = read(filename)
    return solve(bots)

if __name__ == "__main__":
    import sys
    print main(sys.argv[1])


