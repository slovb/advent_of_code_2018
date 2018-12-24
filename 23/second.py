class Bot():
    def __init__(self, p, r):
        self.p = p
        self.r = r

class Box():
    def __init__(self, p, s):
        self.p = p
        self.s = s # side, s = 1 means it only contains itself
        self.bots = []

    def __repr__(self):
        return "{} {} {} {}".format( \
            self.p, \
            self.s, \
            len(self.bots), \
            sum(map(abs, self.p)))

    def add(self, bot):
        if self.close(bot):
            self.bots.append(bot)

    def close(self, bot):
        r = (self.s - 1) / 2
        pr = lambda i: max(0, abs(bot.p[i] - self.p[i]) - r)
        return sum([pr(i) for i in range(3)]) <= bot.r
    
    def deviate(self, dx, dy, dz):
        return (self.p[0]+dx, self.p[1]+dy, self.p[2]+dz)

    def subdivide(self):
        boxes = []
        s = self.s / 3
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    box = Box(self.deviate(i*s, j*s, k*s), s)
                    for bot in self.bots:
                        box.add(bot)
                    boxes.append(box)
        return boxes

def find_bound_side(bots):
    # Unsure
    d = 0
    for bot in bots:
        d = max(d, max(map(abs, bot.p)) + bot.r)
    s_min = 2*d - 1
    s = 1
    while s < s_min:
        s *= 3
    return s

def solve(bots):
    # start with a bound box, the subdivide and keep best
    start = (0,0,0)
    s = find_bound_side(bots)
    bound = Box(start, s)
    for bot in bots:
        bound.add(bot)
    if len(bots) != len(bound.bots):
        print 'Error bounding'
        exit()
    queue = [bound]
    while s > 1:
        l = 0
        q = []
        for box in queue:
            parts = box.subdivide()
            for part in parts:
                l = max(l, len(part.bots))
                q.append(part)
        queue = filter(lambda box: len(box.bots) >= l, q)
        s = queue[0].s
        print s, len(queue), l
    dist = lambda box: sum(map(abs, box.p))
    return min(queue, key=dist)

def read(filename):
    import re
    extract = lambda l: map(int, re.findall(r'-?\d+', l))
    with open(filename, 'r') as f:
        lines = map(extract, f.readlines())
        bots = []
        for bot in [(tuple(l[:3]), l[3]) for l in lines]:
            p = bot[0]
            r = bot[1]
            bots.append(Bot(p, r))
        return bots

def main(filename):
    """
    box = Box((0,0,0), 3)
    box.add(Bot((0,0,0), 2))
    boxes = box.subdivide()
    print box
    for box in boxes:
        print box
    exit()
    """
    bots = read(filename)
    return solve(bots)

if __name__ == "__main__":
    import sys
    print main(sys.argv[1])

