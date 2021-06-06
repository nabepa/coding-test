# python도 통과 하기는 하지만 너무 느림, pypy 제줄
n = int(input())

scores = []
for _ in range(n):
    name, kor, eng, math = input().split()
    scores.append((name, int(kor), int(eng), int(math)))

# sort 쓰는 법
scores.sort(key=lambda score: (-score[1], score[2], -score[3], score[0]))
for score in scores:
    print(score[0])

'''
input
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90

output
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
'''
