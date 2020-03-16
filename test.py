from datetime import datetime
aday = datetime.strptime('18:19', '%H:%M')
bday = datetime.strptime('20 19', '%H %M')
cday = datetime.strptime('16 19', '%H %M')
print((cday - bday).seconds // 3600)

from datetime import datetime
def calcuSleepAwake(time):  # input: [str-TimeA, str-TimeB,...], output: wake-int sleep-int
    sTime = 0
    wTime = 0

    for i in range(0, len(time), 2):
        aday = datetime.strptime(time[i], '%H:%M')
        bday = datetime.strptime(time[i + 1], '%H:%M')
        if i + 2 <= len(time) - 1:
            cday = datetime.strptime(time[i + 2], '%H:%M')
            wTime += (cday - bday).seconds // 60
        sTime += (bday - aday).seconds // 60
    return wTime, sTime



calcuSleepAwake(['05:00', '06:00', '20:00', '08:30', '01:00', '01:30'])
