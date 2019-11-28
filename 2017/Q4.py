#Name: Zacchary Dempsey-Plante
#Date: 2017-02-22
#Question: Favourite Times

currentHours = 12
currentHoursString = str(currentHours)
currentMinutes = 0
timeObserved = int(input())
arithmeticSequences = 0

for t in range(timeObserved):
    #Increment the time
    currentMinutes += 1
    if currentMinutes >= 60:
        currentMinutes -= 60
        currentHours += 1
        if currentHours > 12:
            currentHours -= 12
        currentHoursString = str(currentHours)
    
    cTime = currentHoursString + ('0' if currentMinutes < 10 else '') + str(currentMinutes)
    seqDiff = None
    stillGood = True
    lastVal = None
    for c in range(len(cTime)):
        thisVal = int(cTime[c])
        if c >= 2:
            if thisVal - lastVal != seqDiff:
                stillGood = False
                break
        else:
            seqDiff = int(cTime[1]) - int(cTime[0])
            c += 1 #skip the second iteration
        lastVal = thisVal
    if stillGood == True:
        arithmeticSequences += 1

print(arithmeticSequences)
