import re

def checkPassword(password,letter,min,max):
    instances = 0
    for i in password:
        if i == letter:
            instances = instances+1
    return min <= instances <= max

data = open("passwords", "r")
passwords = [re.match("^(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z]): (?P<password>.*)",x).groupdict() for x in data.readlines()]

validPasswords = 0
for p in passwords:
    if checkPassword(p["password"],p["letter"],int(p["min"]),int(p["max"])):
        validPasswords = validPasswords + 1

print(validPasswords)
