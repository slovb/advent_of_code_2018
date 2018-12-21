from sets import Set
def run(i):
    first = None
    least = float('Inf')
    last = None

    mem = Set()
    ip = 4
    reg = [i] + ([0]*5)

    skipTo8 = False
    reg[1] == 0 # 5
    while True:
        if not skipTo8:
            reg[5] = reg[1] | 65536 # 6
            reg[1] = 8595037 # 7
        else:
            skipTo8 = False
        reg[3] = reg[5] & 255 # 8
        reg[1] += reg[3] # 9
        reg[1] &= 16777215 # 10
        reg[1] *= 65899 # 11
        reg[1] &= 16777215 # 12
        reg[3] = int(256 > reg[5]) # 13
        if not 256 > reg[5]:
            reg[3] = 0 # 17
            while True:
                reg[2] = reg[3] + 1 # 18
                reg[2] *= 256 # 19
                reg[2] = int(reg[2] > reg[5]) # 20
                if reg[2] == 0:
                    reg[3] += 1 # 24
                    # loop to 18
                else:
                    reg[5] = reg[3] # 26
                    skipTo8 = True
                    break
        else:
            if reg[1] in mem:
                print "first {}, last {}, least {}".format(first, last, least)
                return least
            else:
                if first is None:
                    first = reg[1]
                last = reg[1]
                mem.add(reg[1])
                if reg[1] < least:
                    least = reg[1]
                    print least
            if reg[0] == reg[1]: # 29
                return True

least = run(124)
#print least
#print run(least)
