data = open("input", "r")
numbers = [int(x) for x in data.readlines()]

preamble = 25

for i in range(preamble,len(numbers)):
    valid = False
    for j in range(i-preamble,i):
        for k in range(i-preamble,i):
            if numbers[j] != numbers[k] and numbers[j]+numbers[k] == numbers[i]:
                valid = True
    if valid == False:
        print(numbers[i])
        exit()
