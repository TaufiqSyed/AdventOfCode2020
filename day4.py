# Validation Functions
def required_fields_check(fields, required_fields):
    return all([required in fields for required in required_fields])

def byr(x):
    return len(x) == 4 and 1920 <= int(x) <= 2002

def iyr(x):
    return len(x) == 4 and 2010 <= int(x) <= 2020

def eyr(x):
    return len(x) == 4 and 2020 <= int(x) <= 2030

def hgt(x):
    unit = x[-2:]
    if unit == 'cm':
        return 150 <= int(x[:-2]) <= 193
    if unit == 'in':
        return 59 <= int(x[:-2]) <= 76
    return False

def hcl(x):
    return x[0] == '#' and \
        len(x) == 7 and \
        all(['a' <= char <= 'f' or '0' <= char <= '9' for char in x[1:]])

def ecl(x):
    return x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pid(x):
    return len(x) == 9 and x.isnumeric()


# Creating passport key-value pairs
with open('day4_input.txt', 'r') as f:
    lines = f.read().splitlines()
passports = [{}]
i = 0
for line in lines:
    if line == '':
        passports.append({})
        i += 1
    else:
        for data in line.split(' '):
            key, value = data.split(':')
            passports[i][key] = value

# Validating passports using functions
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_count_part1 = 0
valid_count_part2 = 0
for passport in passports:
    fields = [data[:3] for data in passport]
    if not required_fields_check(fields, required_fields):
        continue
    valid_count_part1 += 1
    if all([byr(passport['byr']),
            iyr(passport['iyr']),
            eyr(passport['eyr']),
            hgt(passport['hgt']),
            hcl(passport['hcl']),
            ecl(passport['ecl']),
            pid(passport['pid'])]):
        valid_count_part2 += 1

print('Part 1: ' + str(valid_count_part1))
print('Part 2: ' + str(valid_count_part2))
