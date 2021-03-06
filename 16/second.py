def addr(reg, data):
    o = [i for i in reg]
    o[data[2]] = reg[data[0]] + reg[data[1]]
    return o

def addi(reg, data):
    o = [i for i in reg]
    o[data[2]] = reg[data[0]] + data[1]
    return o

def mulr(reg, data):
    o = [i for i in reg]
    o[data[2]] = reg[data[0]] * reg[data[1]]
    return o

def muli(reg, data):
    o = [i for i in reg]
    o[data[2]] = reg[data[0]] * data[1]
    return o

def banr(reg, data):
    o = [i for i in reg]
    o[data[2]] = reg[data[0]] & reg[data[1]]
    return o

def bani(reg, data):
    o = [i for i in reg]
    o[data[2]] = reg[data[0]] & data[1]
    return o

def borr(reg, data):
    o = [i for i in reg]
    o[data[2]] = reg[data[0]] | reg[data[1]]
    return o

def bori(reg, data):
    o = [i for i in reg]
    o[data[2]] = reg[data[0]] | data[1]
    return o

def setr(reg, data):
    o = [i for i in reg]
    o[data[2]] = reg[data[0]]
    return o

def seti(reg, data):
    o = [i for i in reg]
    o[data[2]] = data[0]
    return o

def gtir(reg, data):
    o = [i for i in reg]
    o[data[2]] = 1 if data[0] > reg[data[1]] else 0
    return o

def gtri(reg, data):
    o = [i for i in reg]
    o[data[2]] = 1 if reg[data[0]] > data[1] else 0
    return o

def gtrr(reg, data):
    o = [i for i in reg]
    o[data[2]] = 1 if reg[data[0]] > reg[data[1]] else 0
    return o

def eqir(reg, data):
    o = [i for i in reg]
    o[data[2]] = 1 if data[0] == reg[data[1]] else 0
    return o

def eqri(reg, data):
    o = [i for i in reg]
    o[data[2]] = 1 if reg[data[0]] == data[1] else 0
    return o

def eqrr(reg, data):
    o = [i for i in reg]
    o[data[2]] = 1 if reg[data[0]] == reg[data[1]] else 0
    return o

def call(op, reg, data):
    if op == 'addr':
        return addr(reg, data)
    elif op == 'addi':
        return addi(reg, data)
    elif op == 'mulr':
        return mulr(reg, data)
    elif op == 'muli':
        return muli(reg, data)
    elif op == 'banr':
        return banr(reg, data)
    elif op == 'bani':
        return bani(reg, data)
    elif op == 'borr':
        return borr(reg, data)
    elif op == 'bori':
        return bori(reg, data)
    elif op == 'setr':
        return setr(reg, data)
    elif op == 'seti':
        return seti(reg, data)
    elif op == 'gtir':
        return gtir(reg, data)
    elif op == 'gtri':
        return gtri(reg, data)
    elif op == 'gtrr':
        return gtrr(reg, data)
    elif op == 'eqir':
        return eqir(reg, data)
    elif op == 'eqri':
        return eqri(reg, data)
    elif op == 'eqrr':
        return eqrr(reg, data)
    print 'ERROR Unknown op {}'.format(op)
    exit()

def match(sample, ops):
    valid = []
    for op in ops:
        if call(op, sample['before'], sample['op'][1:]) == sample['after']:
            valid.append(op)
    return valid

def solve(samples, program):
    ops = [
        'addr', 'addi', 'mulr', 'muli',
        'banr', 'bani', 'borr', 'bori',
        'setr', 'seti', 'gtir', 'gtri',
        'gtrr', 'eqir', 'eqri', 'eqrr',
    ]
    # which ops provide a valid match for each sample
    valid = {}
    for i in range(16):
        valid[i] = [o for o in ops]
    for sample in samples:
        o = sample['op'][0]
        valid[o] = match(sample, valid[o])
    # reduce the valid list
    decoded = {}
    while len(valid) > 0:
        items = valid.items()
        for o, v in items:
            if len(v) == 1:
                val = v[0]
                decoded[o] = val
                del valid[o]
                for _, u in valid.items():
                    if val in u:
                        u.remove(val)
    # run the program
    reg = [0, 0, 0, 0]
    for line in program:
        op = decoded[line[0]]
        data = line[1:]
        reg = call(op, reg, data)
    return reg[0]


def read(filename):
    with open(filename, 'r') as f:
        samples = []
        program = []
        lines = [l.strip() for l in f.readlines()]
        k = 0
        collecting_samples = True
        import re
        splitter = lambda l: map(int, re.findall(r'\d+', l))
        while k < len(lines):
            if collecting_samples and lines[k] == '':
                collecting_samples = False
                k += 2
            if collecting_samples:
                samples.append({
                    'before': splitter(lines[k]),
                    'op': splitter(lines[k+1]),
                    'after': splitter(lines[k+2]),
                })
                k += 3
            else:
                program.append(splitter(lines[k]))
            k += 1
        return samples, program

def main(filename):
    samples, program = read(filename)
    return solve(samples, program)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        unittest.main()
    for a in sys.argv[1:]:
        print main(a)

