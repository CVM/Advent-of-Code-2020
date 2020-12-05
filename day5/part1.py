data = open("input", "r")
boardingPasses = data.read().rstrip().split("\n")

seats = []

for boardingPass in boardingPasses:
    rowMin = 0
    rowMax = 127
    colMin = 0
    colMax = 7
    for i in boardingPass:
        if i == 'F':
            rowMax = rowMax - (rowMax + 1 - rowMin)/2
        if i == 'B':
            rowMin = rowMin + (rowMax + 1 - rowMin)/2
        if i == 'L':
            colMax = colMax - (colMax + 1 - colMin)/2
        if i == 'R':
            colMin = colMin + (colMax + 1 - colMin)/2

    seats.append(int(rowMax * 8 + colMax))

seats.sort()

print(max(seats))
