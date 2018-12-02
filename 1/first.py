def solve(data):
    return sum(data)

def read(filename):
    with open(filename, 'r') as f:
        return [int(l) for l in f.readlines()]

def main (filename):
    return solve(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))

