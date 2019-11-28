villages = int(input())
villagePositions = []
for i in range(villages):
    villagePositions.append(int(input()))
villagePositions.sort()
smallestNeighbourhood = float('inf')
for v in range(1, villages - 1):
    neighbourhoodSize = ((villagePositions[v] - villagePositions[v - 1]) / 2) + ((villagePositions[v + 1] - villagePositions[v]) / 2)
    if neighbourhoodSize < smallestNeighbourhood:
        smallestNeighbourhood = neighbourhoodSize
print(round(smallestNeighbourhood, 1))
