class Node:
    def __init__(self):
        self.children = []
        self.metadata = []

    def value(self):
        l = len(self.children)
        if l == 0:
            return sum(self.metadata)
        val = 0
        for k in self.metadata:
            if k-1 < l:
                val += self.children[k-1].value()
        return val

def read_node(data):
    num_children = data[0]
    num_metadata = data[1]
    n = Node()
    data = data[2:]
    for i in range(num_children):
        m, data = read_node(data)
        n.children.append(m)
    for i in range(num_metadata):
        n.metadata.append(data[i])
    return n, data[num_metadata:]

def solve(data):
    root = read_node(data)[0]
    return root.value()

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

