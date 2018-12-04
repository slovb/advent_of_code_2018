def distance(start, stop):
    return (stop - start).total_seconds() / 60.0

def sleepy(schedule):
    sleeptime = {}
    worst = -float('Inf')
    worstGuard = None
    for event in schedule:
        guard = event['guard']
        time = distance(event['start'], event['stop'])
        if event['guard'] not in sleeptime:
            sleeptime[event['guard']] = 0
        sleeptime[guard] += time;
        if sleeptime[guard] > worst:
            worst = sleeptime[guard]
            worstGuard = guard
    print worstGuard
    return worstGuard

def solve(schedule):
    guard = sleepy(schedule)
    events = list(filter(lambda x: x['guard'] == guard, schedule))
    minutes = {}
    most = 0
    mostKey = None
    for event in events:
        for m in range(event['start'].minute, event['stop'].minute):
            if m not in minutes:
                minutes[m] = 0
            minutes[m] += 1
            if minutes[m] > most:
                most = minutes[m]
                mostKey = m
    return mostKey

def process(rows):
    """process the rows and build a schedule"""
    # current state
    current_guard = None
    sleeping = False
    start = None
    # handle time data as datetime
    # I saw the 23:58 begin time in test data and figured I wanted date classes
    from datetime import datetime
    dateformat = '[%Y-%m-%d %H:%M]'
    schedule = []
    for row in rows:
        parts = row.split()
        time = datetime.strptime(' '.join(parts[0:2]), dateformat)
        if parts[2] == 'Guard':
            if sleeping: # shouldn't happen
                print('Messy input?!')
                schedule.append({
                    'guard': current_guard,
                    'start': start,
                    'stop': time,
                })
                start = None
            current_guard = int(parts[3].strip('#'))
        elif parts[2] == 'falls':
            start = time
            sleeping = True
        elif parts[2] == 'wakes':
            if sleeping:
                schedule.append({
                    'guard': current_guard,
                    'start': start,
                    'stop': time,
                })
                sleeping = False
            else:
                print('Messy input!?')
    return schedule

def read(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines.sort()
        return process(lines)

def main (filename):
    return solve(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print(main(f))

