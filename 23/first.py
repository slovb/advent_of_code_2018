def distance(u, v):
    return sum([abs(u[i]-v[i]) for i in range(len(u))])

def solve(bots):
    signal = lambda bot: bot[1]
    bigbot = max(bots, key=signal)
    in_range = lambda bot: distance(bot[0], bigbot[0]) <= bigbot[1]
    return len(filter(in_range, bots))

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

