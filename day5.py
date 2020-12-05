def find_binary_partition(low, high, l_char, h_char, string):
    for char in string:
        mid = (low + high) // 2
        if char == l_char:
            high = mid
        elif char == h_char:
            low = mid + 1
    if low != high:
        print('ERROR')
        return -1
    return low


with open('day5_input.txt', 'r') as f:
    seat_codes = f.read().splitlines()

seat_ids = []
for seat_code in seat_codes:
    row = find_binary_partition(0, 127, 'F', 'B', seat_code[:7])
    col = find_binary_partition(0, 7, 'L', 'R', seat_code[7:])

    seat_ids.append(row * 8 + col)

print('Part 1: ' + str(max(seat_ids)))

seat_ids.sort()
for a, b in zip(seat_ids, seat_ids[1:]):
    if b - a == 2:
        print("Part 2: " + str(a + 1))
