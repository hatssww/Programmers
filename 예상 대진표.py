from math import ceil

def next(num):
    if num % 2 == 1:
        num = num//2 + 1
    elif num % 2 == 0:
        num = num//2
    return num

def solution(n,a,b):
    cnt = 1
    while n > 2:
        if abs(a - b) == 1 and ceil(a / 2) == ceil(b / 2):
            break
        a = next(a)
        b = next(b)
        cnt += 1
        n //= 2
            
    return cnt


print(solution(8, 4, 7))
print(solution(8, 1, 2))
print(solution(8, 2, 3))


# 간편한 풀이
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer