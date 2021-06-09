# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1

    failure = []
    player = info[N + 1]
    for i in range(N, 0, -1):
        player += info[i]
        if player == 0:
            failure.append((0, i))
        else:
            failure.append((info[i] / player, i))

    failure.sort(key=lambda x: (-x[0], x[1]))
    result = [x[1] for x in failure]
    return result


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
