from bisect import bisect_left, bisect_right


def count_by_range(array, a, b):
    start = bisect_left(array, a)
    end = bisect_right(array, b)
    return end - start


def solution(words, queries):
    array = [[] for _ in range(1000001)]
    reversed_array = [[] for _ in range(1000001)]
    for word in words:
        print(len(word))
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[-1::-1])

    result = []

    for i in range(1, 10001):
        array[i].sort()
        reversed_array[i].sort()

    for query in queries:
        if query[0] == '?':
            cnt_wildcard = query.count('?')
            query = query[-1::-1]
            query = query.split('?')[0]
            a = query + 'a' * cnt_wildcard
            b = query + 'z' * cnt_wildcard
            result.append(count_by_range(reversed_array[len(a)], a, b))
        else:
            cnt_wildcard = query.count('?')
            query = query.split('?')[0]
            a = query + 'a' * cnt_wildcard
            b = query + 'z' * cnt_wildcard
            result.append(count_by_range(array[len(a)], a, b))

    return result


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))
