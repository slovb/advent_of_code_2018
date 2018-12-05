def solve(polymer):
    state = []
    for c in polymer:
        if len(state) == 0 or state[-1] != c.swapcase():
            state.append(c)
        else:
            state.pop()
    return len(state)

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

