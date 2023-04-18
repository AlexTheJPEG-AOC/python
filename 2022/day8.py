trees = []
while True:
    try:
        trees.append([int(i) for i in input()])
    except EOFError:
        break

# The edges are visible
visible = (len(trees[0]) * 2)  # The top and bottom rows
visible += 2 * (len(trees) - 2)  # The left and right columns

scenic_scores = []


def visible_score(v_list, reverse):
    # Returns the scenic subscore of a tree, given all the trees in a certain direction.
    if reverse:
        v_list = list(reversed(v_list))
    if False in v_list:
        return len(v_list[:v_list.index(False)]) + 1
    return len(v_list)


for row in range(1, len(trees) - 1):
    for col in range(1, len(trees[0]) - 1):
        current_tree = trees[row][col]

        # left, right, top, bottom
        visible_list = [False, False, False, False]

        # Check left trees
        visible_left_trees = [trees[row][c] < current_tree for c in range(col)]
        left_score = visible_score(visible_left_trees, True)
        if all(visible_left_trees):
            visible_list[0] = True

        # Check right trees
        visible_right_trees = [trees[row][c] < current_tree for c in range(col + 1, len(trees[0]))]
        right_score = visible_score(visible_right_trees, False)
        if all(visible_right_trees):
            visible_list[1] = True

        # Check top trees
        visible_top_trees = [trees[r][col] < current_tree for r in range(row)]
        top_score = visible_score(visible_top_trees, True)
        if all(visible_top_trees):
            visible_list[2] = True

        # Check bottom trees
        visible_bottom_trees = [trees[r][col] < current_tree for r in range(row + 1, len(trees))]
        bottom_score = visible_score(visible_bottom_trees, False)
        if all(visible_bottom_trees):
            visible_list[3] = True

        # Check if tree is visible from any direction
        if any(visible_list):
            visible += 1
        
        scenic_scores.append(left_score * right_score * top_score * bottom_score)

print(visible)
print(max(scenic_scores))
