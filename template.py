def solve(data):
    return 0

def read(filename):
    #import re
    #extract = lambda l: map(int, re.findall(r'\d+', l))
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines

def main(filename):
    rows = read(filename)
    return solve(rows)

if __name__ == "__main__":
    import sys
    print main(sys.argv[1])

