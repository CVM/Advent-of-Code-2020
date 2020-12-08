import re
data = open("input", "r")
instructions = data.read().rstrip().split("\n")

accumulator = 0
executed = []
index = 0

while True:
    if index in executed:
        print(accumulator)
        exit()

    executed.append(index)
    cmd, opt = instructions[index].split()
    if cmd == 'acc':
        accumulator += int(opt)
    if cmd == 'jmp':
        index += int(opt)
        continue

    index += 1
