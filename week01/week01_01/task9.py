def sum_matrix(m):
    sum_matrix = 0
    for row in m:
        sum_matrix += sum(row)
    return sum_matrix


# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# #print(m.len())
# sum_matrix(m)

# m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# sum_matrix(m)

# m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
# sum_matrix(m)
