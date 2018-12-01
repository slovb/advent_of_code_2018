def solve(data):
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
    if len(data) == 0:
        print "Error: No data"
        exit()
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
    I realized that every loop the entries would effectively increase by
    sum(data).
    
    Therefore the problem is reduced to finding the first entry that has
    the shortest distance to another in sum(data) sized steps.
    
    Two such entries x, y must therefore satisfy x % sum == y % sum.
    """
    step = val
    bestDst = float('Inf') # best (shortest) recorded distance
    bestKey = float('Inf') # key of the second entry with the best distance
    best = float('NaN') # the value of the first entry with the best distance
    modded = [i % step for i in memo]
    for i in range(len(memo)):
        for j in range(i):
            if modded[i] == modded[j]:
                dst = memo[j] - memo[i] / step
                if dst < 0:
                    continue
                if dst < bestDst or (dst == bestDst and i < bestKey):
                    bestDst = dst
                    bestKey = i
                    best = memo[j]
    return best

