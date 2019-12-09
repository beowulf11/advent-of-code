from datetime import datetime


class ShiftInfo:
    def __init__(self, _guard_id, _time_stamp, _info):
        self.guardId = _guard_id
        self.timeStamp = datetime.strptime(_time_stamp[1: -1], '%Y-%m-%d %H:%M')
        self.info = _info
        self.shifts = []

    def __repr__(self):
        return str(self.timeStamp) + " " + str(self.guardId) + " " + str(self.info)

def guard(info):
    fS = -1
    if "Guard" in info:
        fS = info.find(" ")
        fS = info.find(" ", fS + 1)
        guardId = int(info[info.find("#") + 1: fS])
    else:
        guardId = None
    return guardId, info[fS + 1:]


stamps = []
with open("input.txt") as file:
    line = file.readline()
    while line:
        firstSpace = line.find(" ")
        nextS = line.find(" ", firstSpace + 1)
        gId, info = guard(line[nextS + 1:-1])
        stamps.append(ShiftInfo(gId, line[:nextS], info))
        line = file.readline()

stamps.sort(key=lambda shift: shift.timeStamp)

guards = dict()

napTime = None
guardId = stamps[0].guardId

durations = dict()

def addDur(gid, start, end):
    print(gid, start, end)
    if gid not in durations:
        durations[gid] = [0 for x in range(0, 60)]
    for x in range(start, end):
        durations[gid][x] += 1

for x in stamps:
    print(x)
    if guardId != x.guardId and x.guardId is not None:
        if napTime is not None:
            addDur(guardId, napTime, x.timeStamp.minute)
            guards[guardId] = guards.get(guardId, 0) + x.timeStamp.minute - napTime

        guardId = x.guardId
        napTime = None
    elif "falls asleep" in x.info:
        if napTime is None:
            napTime = x.timeStamp.minute
    elif napTime is not None:
        addDur(guardId, napTime, x.timeStamp.minute)
        guards[guardId] = guards.get(guardId, 0) + x.timeStamp.minute - napTime
        napTime = None

for x in durations:
    print(x, durations[x])

m = 0
ids = 0

for x in guards:
    if m < guards[x]:
        m = guards[x]
        ids = x

m = 0
idd = 0
ids = 0
for d in durations:
    for x in range(0, 60):
        if m < durations[d][x]:
            m = durations[d][x]
            idd = x
            ids = d

print(idd * ids, m)

