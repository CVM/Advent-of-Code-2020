import re
data = open("input", "r")
passports = data.read().rstrip().split("\n\n")

required = [
    'byr:19([2-9][0-9])|200[0-2]( |\n|$)',
    'iyr:20(1[0-9]|20)( |\n|$)',
    'eyr:20(2[0-9]|30)( |\n|$)',
    'hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)( |\n|$)',
    'hcl:#[0-9a-f]{6}( |\n|$)',
    'ecl:(amb|blu|brn|gry|grn|hzl|oth)( |\n|$)',
    'pid:[0-9]{9}( |\n|$)'
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
