class Shared():
    def __init__(self, depth, start, target):
        self.depth = depth
        self.start = start
        self.target = target
        self.memory = {}

def erosion_level((x, y), shared):
    depth = shared.depth
    start = shared.start
    target = shared.target
    memory = shared.memory
    position = (x, y)
    # memoization
    if position in memory:
        return memory[position]
    # geological index
    if position == start:
        gi = 0
    elif position == target:
        gi = 0
    elif y == 0:
        gi = 16807 * x
    elif x == 0:
        gi = 48271 * y
    else:
        recurse = lambda x, y: erosion_level((x, y), shared)
        gi = recurse(x-1, y) * recurse(x, y-1)
    # remember and output
    memory[position] = (depth + gi) % 20183
    return memory[position]

def fastest(shared):
    # legend
    # x, y position
    # t time
    # e equipment
    queue = []
    goal = (shared.target[0], shared.target[1], 1) # x y e
    from heapq import heappush, heappop
    def push(t, x, y, e):
        heappush(queue, (t, x, y, e))
    def pop():
        return heappop(queue)
    push(0, shared.start[0], shared.start[1], 1) # t x y e
    path_mem = {}
    def search((t, x, y, e)):
        xye = (x, y, e)
        region = lambda x, y: erosion_level((x, y), shared) % 3
        if xye in path_mem and path_mem[xye] <= t:
            return None # better path found
        elif goal in path_mem and path_mem[goal] <= t:
            return None # way too far away
        elif x < 0 or y < 0 or region(x, y) == e:
            return None # out of bound or wrong equipment
        path_mem[xye] = t
        push(t + 1, x, y + 1, e)
        push(t + 1, x + 1, y, e)
        push(t + 1, x - 1, y, e)
        push(t + 1, x, y - 1, e)
        push(t + 7, x, y, (e + 1) % 3)
        push(t + 7, x, y, (e + 2) % 3)
    while len(queue) > 0:
        search(pop())
    return path_mem[goal]

def solve(depth, target):
    # r type, equipment
    # 0 rocky, neither
    # 1 wet, torch
    # 2 narrow, climbing gear
    # this means if type == equipment, then equip has to be changed
    start = (0, 0)
    shared = Shared(depth, start, target)
    return fastest(shared)

if __name__ == '__main__':
    import sys
    int_arg = lambda k: int(sys.argv[k])
    depth = int_arg(1)
    target = (int_arg(2), int_arg(3))
    print solve(depth, target)
