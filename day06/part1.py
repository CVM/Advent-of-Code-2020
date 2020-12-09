data = open("input", "r")
forms = data.read().rstrip().split("\n\n")

answers = 0

for form in forms:
    answers += len(set(form.replace("\n","")))

print(answers)
