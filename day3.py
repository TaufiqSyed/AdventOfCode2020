def slope_tree_count(x_vector, y_vector):
    tree_count = 0
    x = 0
    for y in range(1, len(geology), y_vector):
        x += x_vector
        x %= line_length
        if geology[y][x] == "#":
            tree_count += 1
    return tree_count


with open("day3_input.txt") as f:
    geology = f.read().splitlines()
line_length = len(geology[0])

print("Part 1: " + str(slope_tree_count(3, 1)))
print("Part 2: " + str(slope_tree_count(1, 1) *
                       slope_tree_count(3, 1) *
                       slope_tree_count(5, 1) *
                       slope_tree_count(7, 1) *
                       slope_tree_count(1, 2)))
