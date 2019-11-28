sunflowers = int(input())
sunflowerData = []
for i in range(sunflowers):
    sunflowerData.append(input().split(' '))
#print(sunflowerData)
def rotTable():
    global sunflowers
    global sunflowerData
    newSunflowerData = [[]] * sunflowers
    for s in range(sunflowers):
        newSunflowerData[s] = [[]] * sunflowers
    for y in range(sunflowers):
        for x in range(sunflowers):
            newSunflowerData[y][x] = sunflowerData[(sunflowers - 1) - x][y]
    sunflowerData = newSunflowerData
for r in range(4):
    done = False
    for s in range(sunflowers - 1):
        if int(sunflowerData[s][0]) > int(sunflowerData[s + 1][0]):
            rotTable()
            break
        if int(sunflowerData[s][0]) > int(sunflowerData[s][1]):
            rotTable()
            rotTable()
            rotTable()
            break
        done = True
    if done:
        break
#print(sunflowerData)
for y in range(sunflowers):
    outLine = ''
    for x in range(sunflowers):
        outLine += (' ' if x > 0 else '') + str(sunflowerData[y][x])
    print(outLine)
