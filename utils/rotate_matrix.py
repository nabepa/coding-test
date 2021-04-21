# 2차원 행렬을 90도로 회전
def rotate_matrix_right(a: list):
    n = len(a)  # length of row
    m = len(a[0])  # length of column
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][j] = a[n - j - 1][i]
    return result


def rotate_matrix_left(a: list):
    n = len(a)  # length of row
    m = len(a[0])  # length of column
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][j] = a[j][m - i - 1]
    return result
