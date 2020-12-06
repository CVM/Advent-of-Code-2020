data = open("input", "r")
forms = data.read().rstrip().split("\n\n")

answers = 0

for form in forms:
    groupAnswers = [set(x) for x in form.split("\n")]

    intersect = groupAnswers[0]
    for i in range(1,len(groupAnswers)):
        intersect = intersect.intersection(groupAnswers[i])

    answers += len(intersect)

print(answers)
