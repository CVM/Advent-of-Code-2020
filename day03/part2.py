data = open("input", "r")
rows = data.read().rstrip().split("\n")

gridWidth = len(rows[0])
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

def getTreesForSlope(slopeX,slopeY):
    xPos = 0
    numTrees = 0

    for i in range(len(rows)):
        if i % slopeY != 0:
            continue
        if rows[i][xPos] == '#':
            numTrees += 1
        xPos = (xPos + slopeX) % gridWidth

    return numTrees

output = 1
for slope in slopes:
    output = output * getTreesForSlope(slope[0],slope[1])

print(output)
