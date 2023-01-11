matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in range(len(matrix)):
#     matrix[i].reverse()
#     print(matrix[i])
for i in range(len(matrix)):
    for j in range(i, len(matrix)):
        print(matrix[i][j])