def addr(reg, data):
    return reg[data[0]] + reg[data[1]]

def addi(reg, data):
    return reg[data[0]] + data[1]

def mulr(reg, data):
    return reg[data[0]] * reg[data[1]]

def muli(reg, data):
    return reg[data[0]] * data[1]

def banr(reg, data):
    return reg[data[0]] & reg[data[1]]

def bani(reg, data):
    return reg[data[0]] & data[1]

def borr(reg, data):
    return reg[data[0]] | reg[data[1]]

def bori(reg, data):
    return reg[data[0]] | data[1]

def setr(reg, data):
    return reg[data[0]]
    return o

def seti(reg, data):
    return data[0]

def gtir(reg, data):
    return 1 if data[0] > reg[data[1]] else 0

def gtri(reg, data):
    return 1 if reg[data[0]] > data[1] else 0

def gtrr(reg, data):
    return 1 if reg[data[0]] > reg[data[1]] else 0

def eqir(reg, data):
    return 1 if data[0] == reg[data[1]] else 0

def eqri(reg, data):
    return 1 if reg[data[0]] == data[1] else 0

def eqrr(reg, data):
    return 1 if reg[data[0]] == reg[data[1]] else 0

def call(reg, (op, data)):
    val = None
    if op == 'addr':
        val = addr(reg, data)
    elif op == 'addi':
        val = addi(reg, data)
    elif op == 'mulr':
        val = mulr(reg, data)
    elif op == 'muli':
        val = muli(reg, data)
    elif op == 'banr':
        val = banr(reg, data)
    elif op == 'bani':
        val = bani(reg, data)
    elif op == 'borr':
        val = borr(reg, data)
    elif op == 'bori':
        val = bori(reg, data)
    elif op == 'setr':
        val = setr(reg, data)
    elif op == 'seti':
        val = seti(reg, data)
    elif op == 'gtir':
        val = gtir(reg, data)
    elif op == 'gtri':
        val = gtri(reg, data)
    elif op == 'gtrr':
        val = gtrr(reg, data)
    elif op == 'eqir':
        val = eqir(reg, data)
    elif op == 'eqri':
        val = eqri(reg, data)
    elif op == 'eqrr':
        val = eqrr(reg, data)
    reg[data[2]] = val

def run(program, ip, initial):
    reg = [0]*6
    for k, v in enumerate(initial):
        reg[k] = v
    while reg[ip] < len(program):
        print reg
        call(reg, program[reg[ip]])
        reg[ip] += 1
    return reg[0]

def read(filename):
    import re
    extract = lambda l: map(int, re.findall(r'\d+', l))
    with open(filename, 'r') as f:
        lines = [(l.split()[0], extract(l)) for l in f.readlines()]
        ip = lines[0][1][0]
        program = lines[1:]
        return program, ip

def main(filename, initial = []):
    program, ip = read(filename)
    return run(program, ip, initial)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2: 
        print main(sys.argv[1])
    elif len(sys.argv) > 2:
        print main(sys.argv[1], map(int, sys.argv[2:]))

