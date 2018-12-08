class Node:
    def __init__(self, num_children, num_metadata):
        self.num_children = num_children
        self.num_metadata = num_metadata
        self.children = []
        self.metadata = []

    def child_sum(self):
        return sum([c.sum() for c in self.children])

    def sum(self):
        return sum(self.metadata) + self.child_sum()

def read_node(data):
    n = Node(data[0], data[1])
    data = data[2:]
    for i in range(n.num_children):
        m, data = read_node(data)
        n.children.append(m)
    for i in range(n.num_metadata):
        n.metadata.append(data[i])
    return n, data[n.num_metadata:]

def solve(data):
    root = read_node(data)[0]
    return root.sum()

def read(filename):
    with open(filename, 'r') as f:
        return [int(n) for n in f.readline().split(' ')]

def main(filename):
    return solve(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))

