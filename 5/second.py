def collapse(polymer):
    state = []
    for c in polymer:
        if len(state) == 0 or state[-1] != c.swapcase():
            state.append(c)
        else:
            state.pop()
    return state

def solve(polymer):
    # collapse the input to get something shorter to work with
    state = collapse(polymer)
    best = len(state)
    # loop through alphabet and filter, collapse, count, compare
    from string import ascii_lowercase
    for c in ascii_lowercase:
        if c in state:
            cswap = c.swapcase()
            candidate = list(filter(lambda x: x != c and x != cswap, state))
            length = len(collapse(candidate))
            if length < best:
                best = length
    return best

def read(filename):
    with open(filename, 'r') as f:
        return "".join(f.readlines()).strip("\n")

def main(filename):
    return solve(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))

