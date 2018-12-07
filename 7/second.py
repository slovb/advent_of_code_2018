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


def solve(poset, max_workers = 5, base_delay = 60):
    alphabet = get_alphabet(poset)
    in_progress = {}
    workers = max_workers
    order = []
    time = 0
    while len(alphabet) + len(in_progress) > 0:
        for key in in_progress.keys(): # extra step needed due to deleting
                                       # while iterating
            in_progress[key] -= 1
            if in_progress[key] == 0:
                order.append(key)
                del in_progress[key]
                workers += 1
        if workers > 0:
            for k, c in enumerate(alphabet):
                if valid(order, c, poset):
                    del alphabet[k]
                    in_progress[c] = base_delay + 1 + ord(c) - ord('A')
                    workers -= 1
                    if workers == 0:
                        break
        time += 1
    return time - 1 # slight doublecounting, needs cleaning up

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

