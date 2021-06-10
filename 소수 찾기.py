from itertools import permutations

def eratos(n):
    check = [False, False] + [True] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if check[i]:
            for j in range(i + i, n + 1, i):
                check[j] = False
    return check

check = eratos(10000000)

def solution(numbers):
    num = [i for i in numbers]
    perm = []
    res = set()
    for i in range(1, len(numbers) + 1):
        for j in list(permutations(num, i)):
            perm.append(j)
    for i in perm:
        tmp = ""
        for j in list(i):
            tmp += j
        if check[int(tmp)]:
            res.add(int(tmp))
    answer = len(res)
    return answer


# set으로 에라토스테네스의 체 사용하는 풀이
from itertools import permutations

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

print(solution("011"))