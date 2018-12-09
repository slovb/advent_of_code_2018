def solve(players, num_marbles):
    magic = 23
    state = [0]
    score = [0] * players
    current = 0
    player = 0
    milestone = 10
    for marble in range(1, num_marbles + 1):
        if not marble % magic == 0:
            current = (current + 2) % len(state)
            state.insert(current, marble)
        else:
            score[player] += marble
            current = (current - 7) % len(state)
            m = state.pop(current)
            score[player] += m
        player = (player + 1) % players
        if marble > milestone:
            print marble
            milestone *= 2
    return max(score)

def read(filename):
    with open(filename, 'r') as f:
        line = f.readline().split()
        return (int(line[0]), int(line[6]))

def main(filename):
    inp = read(filename)
    return solve(inp[0], inp[1])

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))

