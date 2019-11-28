#Name: Zacchary Dempsey-Plante
#Date: 2017-02-22
#Question: Exactly Electrical

import math

startPos = input()
startPos = startPos.split(' ')
startPos = (int(startPos[0]), int(startPos[1]))

endPos = input()
endPos = endPos.split(' ')
endPos = (int(endPos[0]), int(endPos[1]))

batteryCharge = int(input())

loopHeight = abs(startPos[0] - endPos[0]) + abs(startPos[1] - endPos[1])
loopWidth = math.floor(abs(batteryCharge - loopHeight) / 2) * 2
#print(loopHeight + loopWidth)

print(('Y' if loopHeight + loopWidth == batteryCharge else 'N'))
