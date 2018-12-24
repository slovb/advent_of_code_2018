def distance(u, v):
    return sum([abs(u[i]-v[i]) for i in range(len(u))])

def num_in_range(position, bots):
    in_range = lambda bot: distance(bot[0], position) <= bot[1]
    return len(filter(in_range, bots))

def remainder(position, bots):
    remaining = lambda bot: max(0, distance(bot[0], position) - bot[1])
    return sum(map(remaining, bots))

def deviate(p, d):
    out = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i != 0 or j != 0 or k != 0:
                    out.append((p[0] + i*d, p[1] + j*d, p[2] + k*d))
    return out

def find_initial(bots):
    def getter(i):
        return lambda bot: bot[0][i]
    x = sum(map(getter(0), bots))/len(bots)
    y = sum(map(getter(1), bots))/len(bots)
    z = sum(map(getter(2), bots))/len(bots)
    return (x, y, z)

def improve_position(position, bots, banned):
    # find best point inside current cover
    queue = [position]
    start = (0,0,0)
    n = num_in_range(position, bots)
    d = distance(start, position)
    from sets import Set
    explored = Set()
    explored.add(position)
    for b in banned:
        explored.add(b)
    while len(queue) > 0:
        c = queue.pop()
        c_n = num_in_range(c, bots)
        if c_n < n:
            continue
        c_d = distance(start, c)
        if c_d > d:
            continue
        elif c_d < d:
            position = c
            d = c_d
            #print position, n, d
        candidates = deviate(position, 1)
        for c in candidates:
            if c not in explored:
                explored.add(c)
                queue.append(c)
    return position

def find_cover_position(position, bots, banned):
    def evaluate(p):
        return num_in_range(p, bots), remainder(p, bots)
    # find cover
    n = num_in_range(position, bots)
    r = remainder(position, bots)
    from sets import Set
    tried = Set()
    tried.add(position)
    for b in banned:
        tried.add(b)
    sl = 10**9 #step length
    while True:
        #print position, n, r
        candidates = deviate(position, sl)
        candidates = filter(lambda p: p not in tried, candidates)
        for c in candidates:
            tried.add(c)
        if len(candidates) == 0:
            if sl == 1:
                break
            sl /= 2
            continue
        updated = False
        for c in candidates:
            c_n, c_r = evaluate(c)
            if c_n > n or (c_n == n and c_r < r):
                updated = True
                n = c_n
                r = c_r
                position = c
        if not updated:
            if sl == 1:
                break
            sl /= 2
            continue
    return position

def solve(bots):
    """
    candidate = [
        (-62993026, 46835957, 25186332),
        (-67029901, 48844893, 26028016),
        (-64517929, 56080660, 36507026),
        (-54913281, 43308871, 19851611),
        (-65256259, 49283743, 24808585),
        (-60945499, 49668815, 21255184),
        (-61205199, 48885123, 21475861),
        (-63736158, 47290738, 27385592),
        (-77064832, 46354458, 31515862),
        (-64068594, 61566426, 27091059),
        (-67837752, 47922200, 17178478),
        (-65104396, 40244201, 37290995),
        (-63585544, 37947675, 17924991),
        (-59632200, 46747818, 25975824),
        (-72042536, 38090479, 27104320),
        (-71086375, 46049792, 32545283),
        (-59410660, 46300438, 14474419),
        (-54828264, 29489441, 21356375),
        (-65208145, 47653752, 26732060),
        (-60669995, 49462294, 13456376),
        (-70655615, 47849519, 28165393),
        (-69304632, 48944751, 26971269),
        (-66128732, 48862038, 16364684),
        (-71124651, 40811424, 25531047),
        (-59836661, 50917324, 25804196),
        (-66540444, 47124795, 28093101),
        (-63065524, 50193535, 16846057),
        (-60044222, 60129613, 23217264),
        (-72714147, 53708136, 30365731),
        (-74860354, 47613256, 24902461),
        (-56134527, 51263162, 17524363),
        (-76674187, 47130981, 27362058),
        (-58410277, 50755950, 25111682),
        (-59699723, 36838679, 24851122),
        (-66608058, 49430622, 37453899),
        (-73469333, 47756297, 24317939),
        (-67734039, 46150318, 27419528),
        (-68761384, 40331815, 24189592),
    ]
    bad = [
        (-102469894, 79001383, -34111870),
        (-124668393, -8774912, 37078419),
        (-145217680, 27589873, -13397377),
        (-94626048, 55652301, -59960031),
        (1136791, 69864355, -145644804),
        (-16067367, 72074374, 61082651),
        (153881181, 106515611, 8458961),
        (156613952, 96990927, 36484139),
        (-171285540, 51495005, 34847344),
        (-100219738, 19975720, -47752233),
        (-52810118, 165896868, 2665464),
        (32916730, 11827806, 11062038),
        (-73715207, 113421752, -27159065),
        (21762057, 162981105, -48968132),
        (161377626, 111068989, 26189051),
        (-60593157, 59069871, -79040264),
        (-2432261, 210539044, 12063378),
        (19062175, -41680136, 37994070),
        (-76462017, 100925427, -29972552),
        (-15213348, 118942237, -86989681),
        (41524537, 128371854, -83924447),
        (-141601824, 10000609, 12047244),
        (38812597, 32862886, 853790),
        (-164265652, 35163747, 17604512),
        (8224997, 91457077, -115001272),
        (-139757652, 46705976, -35909773),
        (-175980828, 54054567, 16310920),
    ]
    """
    best_n = 0
    best_d = 0
    #bots = filter(lambda b: b[0] not in bad, bots)

    banned = []
    for i in range(5):
    #for position in candidate:
        #position = (0,0,0)
        position = (15972001, 44657551, 29285969)
        #position = find_initial(bots)
        position = find_cover_position(position, bots, banned)
        position = improve_position(position, bots, banned)
        n = num_in_range(position, bots)
        d = distance((0,0,0), position)
        if n > best_n or (n == best_n and d < best_d):
            best_n = n
            best_d = d
            print '!', n, d, position
        else:
            print '?', n, d, position
        banned.append(position)
    return best_n, best_d

def read(filename):
    import re
    extract = lambda l: map(int, re.findall(r'-?\d+', l))
    with open(filename, 'r') as f:
        lines = map(extract, f.readlines())
        return [(tuple(l[:3]), l[3]) for l in lines]

def main(filename):
    bots = read(filename)
    return solve(bots)

if __name__ == "__main__":
    import sys
    print main(sys.argv[1])

