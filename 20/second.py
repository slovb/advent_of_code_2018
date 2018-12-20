def parse(s, mem, x = 0, y = 0):
    xd = 0
    yd = 0
    p = lambda: (x+xd, y+yd)
    i = 0
    depth = 0
    j = None
    while i < len(s):
        if s[i] == '^' or s[i] == '$':
            pass
        elif s[i] == '(':
            if depth == 0:
                j = i
            depth += 1
        elif s[i] == ')':
            depth -= 1
            if depth == 0:
                parse(s[j+1:i], mem, x + xd, y + yd)
        elif depth > 0:
            pass
        elif s[i] == '|':
            xd = 0
            yd = 0
        else:
            if s[i] == 'N':
                yd -= 1
                mem[p()] = '-'
                yd -= 1
            elif s[i] == 'E':
                xd += 1
                mem[p()] = '|'
                xd += 1
            elif s[i] == 'S':
                yd += 1
                mem[p()] = '-'
                yd += 1
            elif s[i] == 'W':
                xd -= 1
                mem[p()] = '|'
                xd -= 1
            mem[p()] = '.'
        i += 1

def limits(memory):
    x, y = zip(*memory.keys())
    return min(x), max(x), min(y), max(y)

def render(memory):
    min_x, max_x, min_y, max_y = limits(memory)
    out = []
    for y in range(min_y - 1, max_y + 2):
        line = []
        for x in range(min_x - 1, max_x + 2):
            p = (x,y)
            if p == (0,0):
                line.append('X')
            elif p in memory:
                line.append(memory[p])
            else:
                line.append('#')
        out.append(''.join(line))
    return '\n'.join(out)

def count(memory, distance):
    x, y = 0, 0
    rooms = {}
    q = [(x, y, 0)] 
    def flood((x, y, current)):
        p = (x, y)
        if p in rooms and rooms[p] <= current:
            return
        rooms[p] = current
        if (x-1, y) in memory:
            q.append((x-2, y, current+1))
        if (x+1, y) in memory:
            q.append((x+2, y, current+1))
        if (x, y-1) in memory:
            q.append((x, y-2, current+1))
        if (x, y+1) in memory:
            q.append((x, y+2, current+1))
    while len(q) > 0:
        flood(q.pop())
    c = 0
    for p, r in rooms.items():
        if r >= distance:
            c += 1
    return c

def solve(data, distance = 1000, debug = False):
    memory = {}
    parse(data, memory)
    if debug:
        print render(memory)
        print count(memory, distance)
    return count(memory, distance)

def read(filename):
    with open(filename, 'r') as f:
        return f.readline().strip()

def main(filename):
    rows = read(filename)
    return solve(rows)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        t = lambda d: solve(d, debug = True)
        #t('(^WNE$)')
        #t('(^ENWWW(NEEE|SSE(EE|N))$)')
        #t('(^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$)')
        t('^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$')
        #t('^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$')
    for a in sys.argv[1:]:
        print main(a)

