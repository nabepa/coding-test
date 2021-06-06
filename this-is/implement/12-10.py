def rotate_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][j] = matrix[n - j - 1][i]
    return result


def check_open(extend_lock):
    len_lock = len(extend_lock) // 3
    for i in range(len_lock, 2 * len_lock):
        for j in range(len_lock, 2 * len_lock):
            if extend_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    len_key = len(key)
    len_lock = len(lock)

    extended_lock = [[0] * (3 * len_lock) for _ in range(3 * len_lock)]
    for i in range(len_lock):
        for j in range(len_lock):
            extended_lock[i + len_lock][j + len_lock] = lock[i][j]

    for _ in range(4):
        for i_lock in range(2 * len_lock):
            for j_lock in range(2 * len_lock):
                for i_key in range(len_key):
                    for j_key in range(len_key):
                        extended_lock[i_lock + i_key][j_lock + j_key] += \
                            key[i_key][j_key]
                if check_open(extended_lock) == True:
                    return True
                for i_key in range(len_key):
                    for j_key in range(len_key):
                        extended_lock[i_lock + i_key][j_lock + j_key] -= \
                            key[i_key][j_key]
        key = rotate_matrix(key)

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
