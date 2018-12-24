def distance(u, v):
    return sum([abs(u[i]-v[i]) for i in range(len(u))])

class Node():
    def __init__(self, p, r):
        self.p = p
        self.r = r
        self.connected = {}

    def close(self, node):
        # true if there exist a point that is in self and node
        # < will be correct because the point is within both
        return self.distance(node.p) < self.r + node.r

    def connect(self, node):
        self.connected[node.p] = node
        node.connected[self.p] = self.p

    def distance(self, u):
        return distance(u, self.p)

def explore(nodes, below):
    bad = []
    for p, node in nodes.items():
        l = len(node.connected)
        if l < below:
            bad.append("{} {}".format(l, p))
    return "\n".join(bad)

def read(filename):
    import re
    extract = lambda l: map(int, re.findall(r'-?\d+', l))
    with open(filename, 'r') as f:
        lines = map(extract, f.readlines())
        nodes = {}
        for bot in [(tuple(l[:3]), l[3]) for l in lines]:
            p = bot[0]
            r = bot[1]
            node = Node(p, r)
            for u, n in nodes.items():
                if node.close(n):
                    node.connect(n)
            nodes[p] = node
        return nodes

def main(filename, below):
    nodes = read(filename)
    return explore(nodes, below)

if __name__ == "__main__":
    import sys
    print main(sys.argv[1], int(sys.argv[2]))

