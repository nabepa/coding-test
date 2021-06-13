# 구간 합을 구하는 알고리즘 중 하나
# P[i]=array[:i]일때, array[L:R]의 구간 합은 P[R]-P[L-1]
# N개의 데이터 M개의 쿼리(M번 구하라고 명령)에 대해 O(NM)을 O(N+M)까지 단축
# index를 0번부터 카운트할지 1번부터 카운터할지에 따라(밑의 구현은 후자) 조금 처리하는 방식이 달라야함
# 교과서랑 다른 풀이
n = 5
data = [10, 20, 30, 40, 50]

prefix_sum = [0] * (n + 1)
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + data[i - 1]

left = 1
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
