qType = int(input(""))
numCitizens = int(input(""))
dcSpeeds = input("").split()
pcSpeeds = input("").split()

for i in range(len(dcSpeeds)):
    dcSpeeds[i] = int(dcSpeeds[i])

for i in range(len(pcSpeeds)):
    pcSpeeds[i] = int(pcSpeeds[i])

if qType == 1:
    dcSpeeds = sorted(dcSpeeds)
    pcSpeeds = sorted(pcSpeeds)
    pFastest = []
    for c in range(numCitizens):
        if dcSpeeds[c] > pcSpeeds[c]:
            pFastest.append(dcSpeeds[c])
        else:
            pFastest.append(pcSpeeds[c])
    totalSpeed = 0
    for i in range(len(pFastest)):
        totalSpeed += pFastest[i]
    print(totalSpeed)
elif qType == 2:
    dcSpeeds = sorted(dcSpeeds, reverse = True)
    pcSpeeds = sorted(pcSpeeds)
    pFastest = []
    for c in range(numCitizens):
        if dcSpeeds[c] > pcSpeeds[c]:
            pFastest.append(dcSpeeds[c])
        else:
            pFastest.append(pcSpeeds[c])
    totalSpeed = 0
    for i in range(len(pFastest)):
        totalSpeed += pFastest[i]
    print(totalSpeed)
