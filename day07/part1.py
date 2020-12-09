import re
data = open("input", "r")
rules = data.read().rstrip().split("\n")

def getBagParents(bag):
    parents = []
    for rule in rules:
        parentBag = re.match("^(.+) bags contain.*"+bag,rule)
        if parentBag != None:
            parents.append(parentBag[1])
            parents = parents + getBagParents(parentBag[1])
    return parents

print(len(set(getBagParents("shiny gold"))))
