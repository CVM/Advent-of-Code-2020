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
        target = numbers[i]
        break

for i in range(len(numbers)):
    nums = []
    nums.append(numbers[i])
    sum = numbers[i]
    for j in range(i+1,len(numbers)):
        nums.append(numbers[j])
        sum += numbers[j]
        if sum > target:
            break
        if sum == target:
            print(min(nums) + max(nums))
            exit()
