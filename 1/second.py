def solve(data):
    step = sum(data)
    # special case: the process loops at exactly the max length
    if step == 0:
        x = 0;
        memo = []
        for i in data:
            memo.append(x)
            x += i
            if (x in memo):
                return x
        print "Error: This shouldn't happen"
        exit()

    # normal cases
    congruence = {} # congruence classes of x mod step
    bestDst = float('Inf') # shortest distance between x and y
    best = float('NaN') # the value that x or y becomes after bestDst
    x = 0
    for k, i in enumerate(data):
        x += i
        xm = x % step
        if xm not in congruence:
            congruence[xm] = []
        for y in congruence[xm]:
            if abs(x - y) < bestDst: # better solution found
                bestDst = abs(x - y)
                # determine which of x, y is the stop
                if step > 0:
                    best = max(x, y) # positive steps => lower -> higher
                else:
                    best = min(x, y) # negative steps => higher -> lower
        congruence[xm] += [x]
    return best

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

def low_memory(data):
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

def multiples(data):
    # memoize the first pass
    val = 0;
    memo = []
    for i in data:
        memo.append(val)
        val += i
        if val in memo:
            return val
    # increase values in memo by multiples of sum and check if a match is found
    s = sum(data)
    n = 1
    while True:
        for m in memo:
            if m + s*n in memo:
                return m + s*n
        n += 1

def modular(data): # solves the problem but fails tests
    # memoize the first pass
    val = 0
    memo = []
    for i in data:
        memo.append(val)
        val += i
        if val in memo:
            return val
    # note val is sum(data) at this point and not 0 because then the function
    # would already have returned
    """
    I realized that every loop the entries of memo would effectively increase
    by sum(data).
    
    Therefore the problem is reduced to finding the first memo entry that has
    the shortest distance to another in sum(data) sized steps.
    
    Two such entries x, y must therefore satisfy x % sum == y % sum.
    """
    step = val
    bestDst = float('Inf')
    best = float('NaN')
    modded = [m % step for m in memo] # memoize memo % step
    for k, x in enumerate(memo):
        for l, y in enumerate(memo[:k]):
            # make sure x and y are congruent modulo step
            if modded[l] != modded[k]:
                continue
            if abs(x - y) < bestDst:
                bestDst = abs(x - y)
                # determine which of x, y is the stop
                if step > 0:
                    best = max(x, y) # positive steps => lower -> higher
                else:
                    best = min(x, y) # negative steps => higher -> lower
    return best

