import re
data = open("input", "r")
passports = data.read().rstrip().split("\n\n")

required = [
    'byr','iyr','eyr','hgt','hcl','ecl','pid'
]
totalValid = 0

for passport in passports:
    valid = 0
    for field in required:
        if re.search(field,passport):
            valid += 1
    if valid == len(required):
        totalValid += 1

print(totalValid)
