def check(name, n):
    letters = {}
    for s in name:
        if s not in letters:
            letters[s] = 0
        letters[s] += 1
    for k, v in letters.items():
        if v == n:
            return 1
    return 0

def solve(data):
    c2 = 0
    c3 = 0
    for name in data:
        c2 += check(name, 2)
        c3 += check(name, 3)
    return c2*c3

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

