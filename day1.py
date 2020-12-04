expenses = []
with open("day1_input.txt") as f:
    for line in f:
        expenses.append(int(line))

n = len(expenses)

for i in range(n):
    for j in range(i + 1, n):
        if expenses[i] + expenses[j] == 2020:
            print("Part 1: " + str(expenses[i] * expenses[j]))
        for k in range(j + 1, n):
            if expenses[i] + expenses[j] + expenses[k] == 2020:
                print("Part 2: " + str(expenses[i] * expenses[j] * expenses[k]))
