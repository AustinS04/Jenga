def findCenterGravity(layerNum):
    yValue = 1.5
    layer = jengaGrid[layerNum]
    if layerNum % 2 == 1:
        layer = [[layer[j][i] for j in range(len(layer))] for i in range(len(layer[0]) - 1, -1, -1)]
    if layer[0] == [1, 1, 1] or layer[0] == [1, 0, 1] or layer[0] == [0, 1, 0]:
        xValue = 1.5
    elif layer[0] == [0, 1, 1]:
        xValue = 2
    elif layer[0] == [1, 1, 0]:
        xValue = 1
    elif layer[0] == [1, 0, 0]:
        xValue = 0.5
    elif layer[0] == [0, 0, 1]:
        xValue = 2.5
    if layerNum % 2 == 1:
        xValue, yValue = yValue, xValue
    return [xValue, yValue]


def findTotalCenterGravity(layerNum):
    xNumerator = 0
    xDenominator = 0
    yNumerator = 0
    yDenominator = 0
    for i in range(layerNum, len(jengaGrid)):
        size = sum(jengaGrid[i][0] + jengaGrid[i][1] + jengaGrid[i][2]) / 3
        xNumerator += size * centGravGrid[i][0]
        yNumerator += size * centGravGrid[i][1]
        xDenominator += size
        yDenominator += size
    return xNumerator / xDenominator, yNumerator / yDenominator


def removePiece(layerNum, num):
    if layerNum % 2 == 0:
        if num == "A":
            for i in range(3):
                jengaGrid[layerNum][i][0] = 0
        elif num == "B":
            for i in range(3):
                jengaGrid[layerNum][i][1] = 0
        elif num == "C":
            for i in range(3):
                jengaGrid[layerNum][i][2] = 0
    else:
        if num == "A":
            for i in range(3):
                jengaGrid[layerNum][0][i] = 0
        elif num == "B":
            for i in range(3):
                jengaGrid[layerNum][1][i] = 0
        elif num == "C":
            for i in range(3):
                jengaGrid[layerNum][2][i] = 0
    if sum(jengaGrid[layerNum][0] + jengaGrid[layerNum][1] + jengaGrid[layerNum][2]) == 0:
        return True
    return False


def addBlock(layerNum, num):
    if len(jengaGrid) == layerNum:
        jengaGrid.append([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    if layerNum % 2 == 0:
        if num == "A":
            for i in range(3):
                jengaGrid[layerNum][i][0] = 1
        elif num == "B":
            for i in range(3):
                jengaGrid[layerNum][i][1] = 1
        elif num == "C":
            for i in range(3):
                jengaGrid[layerNum][i][2] = 1
    else:
        if num == "A":
            for i in range(3):
                jengaGrid[layerNum][0][i] = 1
        elif num == "B":
            for i in range(3):
                jengaGrid[layerNum][1][i] = 1
        elif num == "C":
            for i in range(3):
                jengaGrid[layerNum][2][i] = 1
    if len(jengaGrid) == layerNum + 1:
        convexHullGrid.append(findConvexHull(len(jengaGrid)-1))
        centGravGrid.append(findCenterGravity(len(jengaGrid)-1))


def findConvexHull(layerNum):
    layer = jengaGrid[layerNum]
    layerY = [0, 3]
    if layerNum % 2 == 1:
        layer = [[layer[j][i] for j in range(len(layer))] for i in range(len(layer[0]) - 1, -1, -1)]
    layerX = [layer[0].index(1), len(layer) - layer[0][::-1].index(1)]
    if layerNum % 2 == 1:
        layerX, layerY = layerY, layerX
    return [layerX, layerY]


jengaGrid = []
for action in range(18):
    square = []
    for j in range(3):
        square.append([1, 1, 1])
    jengaGrid.append(square)
centGravGrid = []
convexHullGrid = []
inputs = []

for action in range(int(input())):
    rawInput = input().split()
    currentBlock = []
    for myInput in rawInput:
        currentBlock.append([int(myInput[:-1]), myInput[-1]])
    inputs.append(currentBlock)

for i in range(len(jengaGrid)):
    centGravGrid.append(findCenterGravity(i))
for j in range(len(jengaGrid)):
    convexHullGrid.append(findConvexHull(j))

toggleFellOver = False
for action in inputs:
    layerRemoved = action[0][0] - 1
    letterRemoved = action[0][1]
    layerAdded = action[1][0] - 1
    letterAdded = action[1][1]
    toggleFellOver = removePiece(layerRemoved, letterRemoved)
    if toggleFellOver:
        print("The tower collapses after removing", str(layerRemoved + 1) + letterRemoved)
        break
    centGravGrid[layerRemoved] = findCenterGravity(layerRemoved)
    convexHullGrid[layerRemoved] = findConvexHull(layerRemoved)
    x, y = findTotalCenterGravity(layerRemoved + 1)
    if x < convexHullGrid[layerRemoved][0][0] or x > convexHullGrid[layerRemoved][0][1] or y < \
            convexHullGrid[layerRemoved][1][0] or y > convexHullGrid[layerRemoved][1][1]:
        print("The tower collapses after removing", str(layerRemoved + 1) + letterRemoved)
        toggleFellOver = True
        break
    addBlock(layerAdded, letterAdded)
    centGravGrid[layerRemoved] = findCenterGravity(layerRemoved)
    convexHullGrid[layerRemoved] = findConvexHull(layerRemoved)
    x, y = findTotalCenterGravity(layerRemoved + 1)
    if x < convexHullGrid[layerRemoved][0][0] or x > convexHullGrid[layerRemoved][0][1] or y < \
            convexHullGrid[layerRemoved][1][0] or y > convexHullGrid[layerRemoved][1][1]:
        print("The tower collapses after placing", str(layerAdded + 1) + letterAdded)
        toggleFellOver = True
        break
if not toggleFellOver:
    print("The tower never collapses")