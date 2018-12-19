"""
def sim():
    s = 0
    x = 1
    y = 1
    target = 21 + (22 * 4) + (11 * 19 * 4) + 10550400
    while True:
        y += 1
        if y > target:
            x += 1
            if x > target:
                return s
            y = 1
        if x * y == target:
            s += x
print sim()
"""

c = 0
target = 10551345
i = 1
while not i > target:
    if target % i == 0:
        c += i
    i += 1
print c
