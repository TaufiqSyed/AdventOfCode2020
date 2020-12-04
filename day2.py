with open("day2_input.txt") as f:
    lines = f.read().splitlines()

valid_count_part1 = 0
valid_count_part2 = 0
for line in lines:
    range_section, char, password = line.split()
    l_bound, u_bound = [int(x) for x in range_section.split('-')]
    char = char[:-1]
    char_count = 0
    for letter in password:
        if letter == char:
            char_count += 1
    if l_bound <= char_count <= u_bound:
        valid_count_part1 += 1

    part2valid = False
    if u_bound <= len(password):
        if password[l_bound - 1] == char:
            part2valid = not part2valid
        if password[u_bound - 1] == char:
            part2valid = not part2valid
    if part2valid:
        valid_count_part2 += 1

print("Part 1: " + str(valid_count_part1))
print("Part 2: " + str(valid_count_part2))