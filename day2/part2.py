import re

def checkPassword(password,letter,pos1,pos2):
    return (password[pos1-1] == letter) ^ (password[pos2-1] == letter)

data = open("passwords", "r")
passwords = [re.match("^(?P<pos1>\d+)-(?P<pos2>\d+) (?P<letter>[a-z]): (?P<password>.*)",x).groupdict() for x in data.readlines()]

validPasswords = 0
for p in passwords:
    if checkPassword(p["password"],p["letter"],int(p["pos1"]),int(p["pos2"])):
        validPasswords = validPasswords + 1

print(validPasswords)
