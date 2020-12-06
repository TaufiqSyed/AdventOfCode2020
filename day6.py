with open('day6_input.txt', 'r') as f:
    groups_answers = [list(group.split()) for group in f.read().split('\n\n')]

part_1, part_2 = 0, 0
for group_answers in groups_answers:
    answer_sets = [set(answer) for answer in group_answers]
    all_answers = set(answer_sets[0])
    shared_answers = set(answer_sets[0])
    for s in answer_sets[1:]:
        all_answers |= s
        shared_answers &= s
    part_1 += len(all_answers)
    part_2 += len(shared_answers)

print('Part 1: ' + str(part_1))
print('Part 2: ' + str(part_2))
