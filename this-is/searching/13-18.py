# https://programmers.co.kr/learn/courses/30/lessons/60058
def divide(w):
    cnt = 0
    for i in range(len(w)):
        if w[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            return w[:i + 1], w[i + 1:]


def check(u):
    cnt = 0
    for i in range(len(u)):
        if u[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            return True
        elif cnt < 0:
            return False


def solution(w):
    if len(w) == 0:
        return ''

    u, v = divide(w)
    if check(u) == True:
        return u + solution(v)
    else:
        u = ['(' if i == ')' else ')' for i in u[1:-1]]
        u = ''.join(u)
        return '(' + solution(v) + ')' + u


print(solution('(()())()'))  # (()())()
print(solution(')('))  # ()
print(solution('()))((()'))  # ()(())()

""" 
# 줄인다면 아래 처럼 줄일 수도 있지만, 개인적으로 위에 풀이가 가독성은 더 좋은듯!
def solution(p):
    if p == '':
        return ''
    is_proper = True
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            is_proper = False
        if cnt == 0:
            if is_proper:
                return p[:i + 1] + solution(p[i + 1:])
            else:
                u = ['(' if i == ')' else ')' for i in p[1:i]]
                u = ''.join(u)
                return '(' + solution(p[i + 1:]) + ')' + u
"""
