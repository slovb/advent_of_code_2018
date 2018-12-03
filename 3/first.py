def process(rows):
    data = {}
    for row in rows:
        parts = row.split()
        i = int(parts[0].strip('#'))
        x = int(parts[2].split(',')[0])
        y = int(parts[2].strip(':').split(',')[1])
        w = int(parts[3].split('x')[0])
        h = int(parts[3].split('x')[1])
        data[i] = {
            'x': x,
            'y': y,
            'w': w,
            'h': h
        }
    return data

def read(filename):
    with open(filename, 'r') as f:
        return process(f.readlines())

def solve(data):
    overlap = 0
    claims = {}
    for k, d in data.items():
        for i in range(d['w']):
            for j in range(d['h']):
                p = (d['x'] + i, d['y'] + j)
                if p not in claims:
                    claims[p] = 1
                else:
                    if claims[p] == 1:
                        overlap += 1
                    claims[p] += 1
    return overlap

def main (filename):
    return solve(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))

