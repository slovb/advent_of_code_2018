class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        if left is None:
            self.left = self
        else:
            self.left = left
        if right is None:
            self.right = self
        else:
            self.right = right

    def go_left(self, steps):
        if steps == 0:
            return self
        return self.left.go_left(steps - 1)

    def go_right(self, steps):
        if steps == 0:
            return self
        return self.right.go_right(steps - 1)

    def append(self, value):
        n = Node(value, self, self.right)
        self.right.left = n
        self.right = n
        return n

    def pop(self):
        self.left.right = self.right
        self.right.left = self.left
        return self, self.right

    # used to debug
    def state(self):
        out = [self.value]
        n = self.right
        while n is not self:
            out.append(n.value)
            n = n.right
        return out

def solve(players, num_marbles):
    magic = 23
    score = [0] * players
    current = Node(0)
    player = 0
    for marble in range(1, num_marbles + 1):
        if not marble % magic == 0:
            current = current.go_right(1).append(marble)
        else:
            score[player] += marble
            old, current = current.go_left(7).pop()
            score[player] += old.value
            del old
        player = (player + 1) % players
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

