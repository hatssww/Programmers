# # BFS를 이용한 풀이
# from collections import deque

# def solution(numbers, target):
#     answer = 0
#     q = deque([[0, 0]])  # [sum, level]
#     while q:
#         s, l = q.popleft()
#         if l > len(numbers):
#             break
#         elif l == len(numbers) and s == target:
#             answer += 1
#         q.append([s + numbers[l - 1], l + 1])
#         q.append([s - numbers[l - 1], l + 1])
#     return answer


# product(중복 순열을 이용한 풀이)
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    print(s)
    return s.count(target)

print(solution([1, 1, 1, 1, 1], 3))