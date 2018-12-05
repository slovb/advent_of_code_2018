def distance(a, b):
    dst = 0
    for k in range(len(a)):
        if a[k] != b[k]:
            dst += 1
    return dst

def in_common(a, b):
    c = ''
    for k in range(len(a)):
        if a[k] == b[k]:
            c += a[k]
    return c

def solve(data):
    c = {}
    for k, v in enumerate(data):
        for u in data[:k]:
            if distance(u, v) <= 1:
                return in_common(u, v)
    print "Error: No solution found"
    exit()

def read(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main(filename):
    return solve(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))

