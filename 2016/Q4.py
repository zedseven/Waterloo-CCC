dTime = input("")

dTime = dTime.split(":")
dTime[0] = int(dTime[0])
dTime[1] = int(dTime[1])

aTime = [0,0]

if ((dTime[0] >= 7 and dTime[0] < 10) or (dTime[0] == 10 and dTime[1] == 0)) or ((dTime[0] >= 15 and dTime[0] < 19) or (dTime[0] == 19 and dTime[1] == 0)):
    aTime = dTime
    aTime[0] += 4

else:
    aTime = dTime
    aTime[0] += 2

if aTime[0] >= 24:
    aTime[0] -= 24

paTime = ""
if aTime[0] < 10:
    paTime += "0"
paTime += str(aTime[0]) + ":" + str(aTime[1])
if aTime[1] < 10:
    paTime += "0"

print(paTime)
