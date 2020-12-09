import re
data = open("input", "r")
instructions = data.read().rstrip().split("\n")

def testProgram(instructions):
    accumulator = 0
    executed = []
    index = 0

    while True:
        if index in executed:
            return None
        if index == len(instructions):
            return accumulator

        executed.append(index)
        cmd, opt = instructions[index].split()
        if cmd == 'acc':
            accumulator += int(opt)
        if cmd == 'jmp':
            index += int(opt)
            continue

        index += 1

for index in range(len(instructions)):
    copy = instructions[:]
    cmd, opt = copy[index].split()
    if cmd == 'nop':
        copy[index] = copy[index].replace("nop","jmp")
    if cmd == 'jmp':
        copy[index] = copy[index].replace("jmp","nop")

    result = testProgram(copy)
    if result:
        print(result)
        exit()
