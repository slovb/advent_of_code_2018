class Group:
    def __init__(self, name, team, n, hp, d, dt, i):
        self.name = name
        self.team = team
        self.n = n
        self.hp = hp
        self.immune = []
        self.weak = []
        self.d = d
        self.dt = dt
        self.i = i
    
    def __repr__(self):
        out = []
        out.append(self.n)
        out.append('units each with')
        out.append(self.hp)
        out.append('hit points')
        a = []
        if len(self.immune) > 0:
            a.append('immune to {}'.format(', '.join(self.immune)))
        if len(self.weak) > 0:
            a.append('weak to {}'.format(', '.join(self.weak)))
        if len(a) > 0:
            out.append('({})'.format('; '.join(a)))
        out.append('with an attack that does')
        out.append(self.d)
        out.append(self.dt)
        out.append('damage at initiative')
        out.append(self.i)
        return " ".join([str(o) for o in out])

    def effective_power(self):
        return self.n * self.d

    def is_alive(self):
        return self.n > 0
    
    def estimate_damage(self, attacker):
        if attacker.dt in self.immune:
            return 0
        d = max(0, attacker.d * attacker.n) # handle negative n
        if attacker.dt in self.weak:
            return 2 * d
        return d

    def get_attacked(self, attacker):
        damage = self.estimate_damage(attacker)
        self.n -= damage/self.hp
        return self

def solve(groups):
    from heapq import heappush, heappop
    def target_priority(a, d): 
        return (d.estimate_damage(a), d.effective_power(), d.i)
    team_immune = lambda g: g.team == 'Immune'
    team_infection = lambda g: g.team == 'Infection'
    len_team_immune = lambda : len(filter(team_immune, groups))
    len_team_infection = lambda : len(filter(team_infection, groups))
    #bout = 1
    while len_team_immune() > 0 and len_team_infection() > 0:
        """
        print '------------------------------------'
        print 'Round: {}'.format(bout)
        print 'Immune System:'
        for g in filter(team_immune, groups):
            print 'Group {} contains {} units'.format(g.name, g.n)
        print 'Infection:'
        for g in filter(team_infection, groups):
            print 'Group {} contains {} units'.format(g.name, g.n)
        print ''
        bout += 1
        """

        q = []
        for g in groups:
            heappush(q, (-g.effective_power(), -g.i, g))
        attacked = {}
        not_attacked = lambda g: g not in attacked
        while len(q) > 0:
            attacker = heappop(q)[-1]
            aggro = lambda d: target_priority(attacker, d)
            if attacker.team == 'Immune':
                target_team = filter(team_infection, groups)
            else:
                target_team = filter(team_immune, groups)
            targets = filter(not_attacked, target_team)
            if len(targets) == 0:
                continue
            target = max(targets, key=aggro)
            if target == None or target.estimate_damage(attacker) == 0:
                continue
            attacked[target] = attacker
        q = []
        for target, attacker in attacked.items():
            heappush(q, (-attacker.i, attacker, target))
        while len(q) > 0:
            _, attacker, target = heappop(q)
            target.get_attacked(attacker)
        groups = filter(lambda g: g.is_alive(), groups)
    return sum([g.n for g in groups])

def read(filename):
    import re
    extract = lambda l: map(int, re.findall(r'-?\d+', l))
    def parenthesis(l): 
        immune = []
        weak = []
        regex = re.findall(r'\((:?.*)\)', l)
        if len(regex) > 0:
            separated = [a.strip(' ').split(' ') for a in regex[0].split(';')]
            for part in separated:
                for typ in part[2:]:
                    if part[0] == 'immune':
                        immune.append(typ.strip(','))
                    else:
                        weak.append(typ.strip(','))
        return immune, weak
    with open(filename, 'r') as f:
        team = None
        groups = []
        name = 1
        for l in f.readlines():
            e = extract(l)
            s = l.split()
            if len(e) == 0:
                if len(s) > 0:
                    if s[0] == 'Immune':
                        team = 'Immune'
                    else:
                        team = 'Infection'
                    name = 1
                continue
            n, hp, d, i = extract(l)
            dt = s[-5]
            g = Group(name, team, n, hp, d, dt, i)
            name += 1
            immune, weak = parenthesis(l)
            for typ in immune:
                g.immune.append(typ)
            for typ in weak:
                g.weak.append(typ)
            groups.append(g)
        return groups

def main(filename):
    groups = read(filename)
    return solve(groups)

if __name__ == "__main__":
    import sys
    print main(sys.argv[1])

