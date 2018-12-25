class Point():
    def __init__(self, x, y, z, t):
        self.x = x
        self.y = y
        self.z = z
        self.t = t
        self.connected = []

    def __repr__(self):
        return "{}\t{}\t{}\t{}".format(self.x, self.y, self.z, self.t)

    def connect(self, p):
        if self.distance(p) <= 3:
            self.connected.append(p)
            p.connected.append(self)

    def distance(self, p):
        return abs(self.x - p.x) + abs(self.y - p.y) + \
               abs(self.z - p.z) + abs(self.t - p.t)

def solve(points):
    seen = []
    count = 0
    for point in points:
        if point in seen:
            continue
        count += 1
        q = [point]
        while len(q) > 0:
            p = q.pop()
            if p in seen:
                continue
            seen.append(p)
            for c in p.connected:
                q.append(c)
    return count

def process(data):
    points = []
    for x, y, z, t in data:
        point = Point(x, y, z, t)
        for p in points:
            point.connect(p)
        points.append(point)
    return points

def read(filename):
    import re
    extract = lambda l: map(int, re.findall(r'-?\d+', l))
    with open(filename, 'r') as f:
        return map(extract, f.readlines())

def main(filename):
    data = read(filename)
    points = process(data)
    return solve(points)

if __name__ == "__main__":
    import sys
    for f in sys.argv[1:]:
        print main(f)


