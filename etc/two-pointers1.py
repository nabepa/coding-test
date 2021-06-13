# 활용 예1) n개의 양수의 정수로된 수열에서 부분합이 m인 연속 수열 찾기
# 양수의 정수로된 수열이이라는 전제 조건이 성립해야 쓸 수 있는 알고리즘
n = 5  # 데이터의 개수
m = 5  # 찾고자 하는 부분 합
data = [1, 2, 3, 2, 5]

end = 0
sum_val = 0
cnt = 0

for start in range(n):
    while sum_val < m and end < n:
        sum_val += data[end]
        end += 1
    if sum_val == m:
        cnt += 1
    sum_val -= data[start]

print(cnt)
