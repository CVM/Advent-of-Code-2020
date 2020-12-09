data = open("input", "r")
rows = data.read().rstrip().split("\n")

xPos = 0
gridWidth = len(rows[0])
numTrees = 0

for row in rows:
    if row[xPos] == '#':
        numTrees += 1
    xPos = (xPos + 3) % gridWidth

print(numTrees)
