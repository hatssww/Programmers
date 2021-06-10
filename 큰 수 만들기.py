# 문제는 풀리는데 시간초과
from itertools import combinations

def solution(number, k):
    n = len(number) - k
    numbers = [i for i in number]
    comb = list(map("".join, combinations(numbers, n)))
    print(comb)

    return max(comb)


# stack 이용
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while stack and num > stack[-1] and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return "".join(stack)
    

print(solution("4177252841", 4))
print(solution("1231234", 3))