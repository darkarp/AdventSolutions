def task1_naive(map_input, up_slope, right_slope):
    i = up_slope
    j = right_slope
    path_len = len(map_input[0]) - 1
    trees = 0
    while i < len(map_input):
        if map_input[i][j] in ["#", "X"]:
            trees += 1
        i += up_slope
        j = (j + right_slope) % path_len
    return trees


def task2_naive(map_input):
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    trees = 1
    for right_slope, up_slope in slopes:
        trees *= task1_naive(map_input, up_slope, right_slope)
    return trees


if __name__ == "__main__":
    map_input = [line for line in open("map.txt", "r")]
    task1 = task1_naive(map_input, 1, 3)
    task2 = task2_naive(map_input)
    print(task1, task2)
