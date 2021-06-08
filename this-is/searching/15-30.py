from bisect import bisect_left, bisect_right


def count_by_range(array, a, b):
    start = bisect_left(array, a)
    end = bisect_right(array, b)
    return end - start


def solution(words, queries):
    reversed_words = []
    for word in words:
        reversed_words.append(word[-1::-1])

    result = []

    for query in queries:
        if query[0] == '?':
            cnt_wildcard = query.count('?')
            query = query[-1::-1]
            query = query.split('?')[0]
            a = query + 'a' * cnt_wildcard
            z = query + 'z' * cnt_wildcard
            result.append(count_by_range(reversed_words, a, z))
        else:
            cnt_wildcard = query.count('?')
            query = query.split('?')[0]
            a = query + 'a' * cnt_wildcard
            z = query + 'z' * cnt_wildcard
            result.append(count_by_range(words, a, z))

    return result
