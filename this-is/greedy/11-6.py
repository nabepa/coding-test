# need to review
# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    elapsed_time = 0
    remain_num = len(food_times)
    prev = 0

    while elapsed_time + (q[0][0] - prev) * remain_num <= k:
        now = heapq.heappop(q)[0]
        elapsed_time += (now - prev) * remain_num
        prev = now
        remain_num -= 1

    result = sorted(q, key=lambda x: x[1])
    return result[(k - elapsed_time) % remain_num][1]
