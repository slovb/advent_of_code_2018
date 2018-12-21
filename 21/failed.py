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

def step(program, ip, reg):
    reg = [0]*6
    reg[0] = initial
    while reg[ip] < len(program):
        print reg
        call(reg, program[reg[ip]])
        reg[ip] += 1
    return initial

def solve(program, ip):
    plength = len(program)
    i = 0
    reg = [i] + ([0]*5)
    # record order of operations for first iteration
    order = []
    for k in range(100):
        order.append(reg[ip])
        call(reg, program[reg[ip]])
        reg[ip] += 1
    # match against following iterations
    i += 1
    while True:
        if i % 10**4 == 0:
            print i
        reg = [i] + ([0]*5)
        for o in order:
            if reg[ip] != o:
                return i
            call(reg, program[reg[ip]])
            reg[ip] += 1
        i += 1

def run(program, ip, i):
    plength = len(program)
    reg = [i] + ([0] * 5)
    while reg[ip] < plength:
        call(reg, program[reg[ip]])
        reg[ip] += 1

def read(filename):
    import re
    extract = lambda l: map(int, re.findall(r'\d+', l))
    with open(filename, 'r') as f:
        lines = [(l.split()[0], extract(l)) for l in f.readlines()]
        ip = lines[0][1][0]
        program = lines[1:]
        return program, ip

def main(filename):
    program, ip = read(filename)
    #return run(program, ip, 15883666)
    #return run(program, ip, 762)
    #return run(program, ip, 3253305)
    return solve(program, ip)

if __name__ == "__main__":
    import sys
    print main(sys.argv[1])

