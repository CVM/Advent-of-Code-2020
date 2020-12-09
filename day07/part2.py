import re
data = open("input", "r")
rules = data.read().rstrip().split("\n")

def getBagsWithin(bag):
    within = []
    for rule in rules:
        childBagsString = re.match("^"+bag+" bags contain (.+)$",rule)
        if childBagsString != None:
            childBags = childBagsString[1].split(", ")
            for childBag in childBags:
                child = re.match("^(\d+) (.+) bag.*$",childBag)
                if child != None:
                    for i in range(0,int(child[1])):
                        within.append(child[2])
                        within = within + getBagsWithin(child[2])
    return within

print(len(getBagsWithin("shiny gold")))
