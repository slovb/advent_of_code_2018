class Shared():
    def __init__(self, depth, start, target):
        self.depth = depth
        self.start = start
        self.target = target
        self.memory = {}

def erosion_level((x, y), shared):
    memory = shared.memory
    # memoization
    if (x, y) in memory:
        return memory[(x, y)]
    depth = shared.depth
    start = shared.start
    target = shared.target
    queue = [(x, y)]
    while len(queue) > 0:
        p = queue.pop()
        # geological index
        if p == start or p == target:
            gi = 0
        elif p[0] == 0 or p[1] == 0:
            gi = 16807 * p[0] + 48271 * p[1]
        else:
            mx = memory.get((p[0] - 1, p[1]), None)
            my = memory.get((p[0], p[1] - 1), None)
            if mx is not None and my is not None:
                gi = mx * my
            else:
                queue.append((p[0], p[1]))
                if mx is None:
                    queue.append((p[0] - 1, p[1]))
                if my is None:
                    queue.append((p[0], p[1] - 1))
                continue
        el = (depth + gi) % 20183
        memory[p] = el
    return memory[(x, y)]

def fastest(shared):
    # legend
    # x, y position
    # t time
    # e equipment
    goal = (shared.target[0], shared.target[1], 1) # x y e
    queue = []
    def distance(x, y, e):
        dx = abs(goal[0]-x)
        dy = abs(goal[1]-y)
        de = abs(goal[2]-e)
        return dx + dy + (7 if de > 0 else 0)
    def heuristic(t, x, y, e):
        return t + distance(x, y, e)
    from heapq import heappush, heappop
    def push(t, x, y, e):
        h = heuristic(t, x, y, e)
        heappush(queue, (h, t, x, y, e))
    def pop():
        return heappop(queue)
    push(0, shared.start[0], shared.start[1], 1) # t x y e
    path_mem = {}
    progress = {'found':False, 'length':None}
    def search((h, t, x, y, e)):
        xye = (x, y, e)
        d = distance(x, y, e)
        if xye == goal:
            path_mem[goal] = min(t, path_mem.get(goal, t))
            progress['found'] = True
            progress['length'] = path_mem[goal]
            return
        region = lambda x, y: erosion_level((x, y), shared) % 3
        if xye in path_mem and path_mem[xye] <= t:
            return # better path found
        elif progress['found'] and progress['length'] - 1 <= t + d:
            return # quicker solution found
        elif x < 0 or y < 0 or region(x, y) == e:
            return # out of bound or wrong equipment
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
