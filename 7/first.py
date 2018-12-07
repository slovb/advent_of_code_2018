def valid(order, character, poset):
    for p in poset:
        if p[1] == character and p[0] not in order:
            return False
    return True

def get_alphabet(poset):
    character = []
    for p in poset:
        if p[0] not in character:
            character.append(p[0])
        if p[1] not in character:
            character.append(p[1])
    character.sort()
    return character


def solve(poset):
    alphabet = get_alphabet(poset)
    order = []
    while len(alphabet) > 0:
        for k, c in enumerate(alphabet):
            if valid(order, c, poset):
                order.append(c)
                del alphabet[k]
                break
    return "".join(order)

def read(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        poset = []
        for l in lines:
            s = l.split()
            poset.append((s[1], s[7]))
        return poset

def main(filename):
    return solve(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))

