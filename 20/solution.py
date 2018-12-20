class Room:
    def __init__(self, p):
        self.p = p
        self.adjacent = []

    def add(self, room):
        if room not in self.adjacent:
            self.adjacent.append(room)
        return self

    def join(self, room):
        self.add(room)
        room.add(self)
        return self

def parse(s):
    start = Room(0)
    room = start
    rooms = {room.p: room}
    stack = []
    for i, c in enumerate(s):
        position = room.p
        if c == '^' or c == '$':
            pass
        elif c == '(':
            stack.append((start, room))
            start = room
        elif c == ')':
            start, room = stack.pop()
        elif c == '|':
            room = start
        else:
            position += {'N': -1j, 'E': 1, 'S': 1j, 'W': -1}[c]
            if position in rooms:
                r = rooms[position]
            else:
                r = Room(position)
                rooms[position] = r
            room.join(r)
            room = r
    return start

def count(start, distance):
    distances = {}
    q = [(start, 0)] 
    def flood((room, current)):
        if room.p in distances and distances[room.p] <= current:
            return
        distances[room.p] = current
        for r in room.adjacent:
            q.append((r, current+1))
    while len(q) > 0:
        flood(q.pop())
    c = 0
    longest = 0
    for p, d in distances.items():
        longest = max(longest, d) 
        if d >= distance:
            c += 1
    return longest, c

def solve(data, distance = 1000):
    start = parse(data)
    return count(start, distance)

def read(filename):
    with open(filename, 'r') as f:
        return f.readline().strip()

def main(filename):
    rows = read(filename)
    return solve(rows)

if __name__ == "__main__":
    import sys
    for a in sys.argv[1:]:
        print main(a)

