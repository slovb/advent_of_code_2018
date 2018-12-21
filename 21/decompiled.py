def run(i):
    ip = 4
    reg = [i] + ([0]*5)

    """
    reg[1] = 123 # 0
    while True:
        reg[1] &= 456 # 1
        reg[1] = int(reg[1] == 72) # 2
        if reg[1] == 1:
            break
    """
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
        reg[ip] = 14
        reg[ip] += reg[3] # 14
        if not 256 > reg[5]:
            reg[ip] += 1; reg[ip] += 1 # 15
            reg[3] = 0 # 17
            while True:
                reg[2] = reg[3] + 1 # 18
                reg[2] *= 256 # 19
                reg[2] = int(reg[2] > reg[5]) # 20
                reg[ip] = 21 + reg[2] # 21
                if reg[2] == 0:
                    reg[ip] += 2 # 22
                    reg[3] += 1 # 24
                    reg[ip] = 17 + 1 # 25
                    # 18
                else:
                    reg[ip] = 25 + 1 # 23
                    reg[5] = reg[3] # 26
                    reg[ip] = 7 + 1 # 27
                    skipTo8 = True
                    break
        else:
            reg[ip] = 27; reg[ip] += 1 # 16
            reg[3] = int(reg[0] == reg[1]) # 28
            if reg[0] == reg[1]: # 29
                return True
            reg[ip] = 5; reg[ip] += 1 # 30
            # loop to 6

