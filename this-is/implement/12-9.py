def solution(s):
    result = len(s)
    for length in range(1, len(s) // 2 + 1):
        compressed = ''
        repeat_cnt = 1
        start = 0
        prev = s[start:length]

        for start in range(length, len(s) + 1, length):
            now = s[start:start + length]
            if prev == now:
                repeat_cnt += 1
            else:
                if repeat_cnt > 1:
                    compressed += str(repeat_cnt)
                compressed += prev
                prev = now
                repeat_cnt = 1
        compressed += s[start:]

        result = min(result, len(compressed))

    return result


print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
