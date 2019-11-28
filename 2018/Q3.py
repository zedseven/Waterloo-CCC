dimensions = input().split(' ')
gridWidth = int(dimensions[1])
gridHeight = int(dimensions[0])
grid = [''] * gridHeight
for y in range(gridHeight):
    grid[y] = input()
startPos = []
for y in range(1, gridHeight - 1):
    for x in range(1, gridWidth - 1):
        if grid[y][x] == 'S':
            startPos = [x, y]
            break
    if len(startPos) > 0:
        break
doneSteps = -1
checkCells = []
def cameraCheck(x, y): #not happy with it, but for now...
    done = False
    c = 1
    while not done:
        if grid[y][x - c] == 'C':
            return True
        elif grid[y][x - c] == 'W':
            done = True
        else:
            c += 1
    done = False
    c = 1
    while not done:
        if grid[y][x + c] == 'C':
            return True
        elif grid[y][x + c] == 'W':
            done = True
        else:
            c += 1
    done = False
    c = 1
    while not done:
        if grid[y - c][x] == 'C':
            return True
        elif grid[y - c][x] == 'W':
            done = True
        else:
            c += 1
    done = False
    c = 1
    while not done:
        if grid[y + c][x] == 'C':
            return True
        elif grid[y + c][x] == 'W':
            done = True
        else:
            c += 1
    return False
def checkCell(x, y, cx, cy, steps):
    global doneSteps
    global checkCells
    print('checking cell: (' + str(x) + ', ' + str(y) + ') - (' + str(cx) + ', ' + str(cy) + ') - ' + grid[y][x])
    if grid[y][x] == 'S':
        doneSteps = steps + 1
        return True
    if grid[y][x] == '.' or (grid[y][x] == 'L' and cx < x) or (grid[y][x] == 'R' and cx > x) or (grid[y][x] == 'U' and cy < y) or (grid[y][x] == 'D' and cy > y):
        if grid[y][x] == '.':
            if cameraCheck(x, y) == False:
                checkCells.append([x, y, cx, cy, steps + 1])
        else:
            checkCells.append([x, y, cx, cy, steps])
def findSteps(x, y):
    global doneSteps
    global checkCells
    print('finding steps: (' + str(x) + ', ' + str(y) + ')')
    if cameraCheck(x, y) == False:
        checkCells.append([x, y, x, y, 0])
        while doneSteps == -1 and len(checkCells) > 0:
            if checkCells[0][2] != checkCells[0][0] - 1 or checkCells[0][3] != checkCells[0][1]:
                checkCell(checkCells[0][0] - 1, checkCells[0][1], checkCells[0][0], checkCells[0][1], checkCells[0][4])
            if checkCells[0][2] != checkCells[0][0] + 1 or checkCells[0][3] != checkCells[0][1] and doneSteps == -1:
                checkCell(checkCells[0][0] + 1, checkCells[0][1], checkCells[0][0], checkCells[0][1], checkCells[0][4])
            if checkCells[0][2] != checkCells[0][0] or checkCells[0][3] != checkCells[0][1] - 1 and doneSteps == -1:
                checkCell(checkCells[0][0], checkCells[0][1] - 1, checkCells[0][0], checkCells[0][1], checkCells[0][4])
            if checkCells[0][2] != checkCells[0][0] or checkCells[0][3] != checkCells[0][1] + 1 and doneSteps == -1:
                checkCell(checkCells[0][0], checkCells[0][1] + 1, checkCells[0][0], checkCells[0][1], checkCells[0][4])
            checkCells.pop(0)
    return doneSteps
for y in range(1, gridHeight - 1):
    for x in range(1, gridWidth - 1):
        if grid[y][x] == '.':
            print(findSteps(x, y))
            doneSteps = -1
            checkCells = []
