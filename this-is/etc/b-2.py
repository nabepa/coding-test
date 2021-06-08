# p.486
# https://www.acmicpc.net/problem/1759
from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')

l, c = map(int, input().split())  # l개의 문자, c종류의 문자
data = input().split()  # 사용된 문자들
data.sort()

result = 0
for candi in combinations(data, l):
    cnt_vowel = 0
    for c in candi:
        if c in vowels:
            cnt_vowel += 1
    if cnt_vowel >= 1 and l - cnt_vowel >= 2:
        print(''.join(candi))

'''
input
4 6
a t c i s w
output
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
'''
