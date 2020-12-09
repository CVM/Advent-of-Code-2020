import re
data = open("input", "r")
boardingPasses = re.sub('F|L','0',re.sub(r'B|R','1',data.read().rstrip())).split("\n")

seats = []

for boardingPass in boardingPasses:
    seats.append(int(boardingPass,2))

seats.sort()

print('Part 1: ' + str(max(seats)))

for i in range(len(seats)):
    if seats[i+1] - seats[i] > 1:
        print('Part 2: ' + str(seats[i]+1))
        exit()
