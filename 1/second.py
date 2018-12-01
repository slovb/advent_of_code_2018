
def solve(data):
    # memoize the first pass
    val = 0;
    memo = []
    for i in data:
        if val in memo:
            return val
        memo.append(val)
        val += i
    # increase values in memo by multiples of sum and check if a match is found
    s = sum(data)
    n = 2
    while True:
        for m in memo:
            if m + s*n in memo:
                return m + s*n
        n += 1

def read(filename):
    with open(filename, 'r') as f:
        return [int(l.rstrip("\n")) for l in f.readlines()]

def main (filename):
    return solve(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))

"""rejected solutions"""
# memoize everything and solve by brute force
def naive(data):
    val = 0;
    memo = []
    while True:
        for i in data:
            if (val in memo):
                return val
            memo.append(val)
            val += i

def lowMemory(data):
    # memoize the first pass through
    val = 0;
    memo = []
    for i in data:
        memo.append(val)
        val += i
        if val in memo:
            return val
    # repeat without memoization until a solution is found.
    # I think there is an algebraic argument why this assumption hold
    # true in general, but I can't formulate it at this point
    while True:
        for i in data:
            val += i
            if val in memo:
                return val

