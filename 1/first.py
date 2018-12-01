def solve(data):
    return sum(data)

def read(filename):
    with open(filename, 'r') as f:
        return [int(l.rstrip("\n")) for l in f.readlines()]

def main (filename):
    return calc(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))
