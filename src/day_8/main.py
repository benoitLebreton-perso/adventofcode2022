import re


def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(matrix[i][j])
        matrix_T.append(row)
    return matrix_T


def greater_than_trees(tree, direction_trees):
    return tree > max(direction_trees, default=-1)


def find_visible_trees(matrix):
    transposed_matrix = transpose(matrix)
    compte_visible = 0
    for i, line in enumerate(matrix):
        for j,tree in enumerate(line):
            visible = False
            left_trees = line[:j]
            left_trees.reverse()
            if greater_than_trees(tree, left_trees):
                visible = True
            right_trees = line[j+1:]
            if greater_than_trees(tree, right_trees):
                visible = True
            down_trees = transposed_matrix[j][i+1:]
            if greater_than_trees(tree, down_trees):
                visible = True
            top_trees = transposed_matrix[j][:i]
            top_trees.reverse()
            if greater_than_trees(tree, top_trees):
                visible = True
            if visible:
                compte_visible+=1
    return compte_visible


def dist_to_block_trees(tree, direction_trees):
    dist = 1
    is_blocked = False
    while not is_blocked and len(direction_trees)>1:
        next_tree = direction_trees.pop(0)
        if tree <= next_tree:
            is_blocked = True
        else:
            dist+=1
    return dist


def best_spot_score(matrix):
    transposed_matrix = transpose(matrix)
    scenic_scores = []
    for i, line in enumerate(matrix):
        for j,tree in enumerate(line):
            if i == 0 or j == 0 or i == len(matrix)-1 or j == len(line)-1:
                scenic_score = 0
            else:
                left_trees = line[:j]
                left_trees.reverse()
                right_trees = line[j+1:]
                down_trees = transposed_matrix[j][i+1:]
                top_trees = transposed_matrix[j][:i]
                top_trees.reverse()
                left_dist = dist_to_block_trees(tree, left_trees)
                right_dist = dist_to_block_trees(tree, right_trees)
                down_dist = dist_to_block_trees(tree, down_trees)
                top_dist = dist_to_block_trees(tree, top_trees)
                scenic_score = left_dist*right_dist*down_dist*top_dist
            scenic_scores.append(scenic_score)
    return max(scenic_scores)


def main():
    input_path = "src/day_9/input.txt"
    with open(input_path, 'r') as f:
        trees = f.read()
    lines_str = trees.split("\n")
    matrix = []
    for l in lines_str:
        line_str = re.findall("(\d)", l)
        line_int = [int(el) for el in line_str]
        matrix.append(line_int)
    compte_visible = find_visible_trees(matrix)
    best_spot_score_ = best_spot_score(matrix)

if __name__ == '__main__':
    main()