# from collections import deque
# def solution(orders, course):
#     a = [(len(orders[i]), set([j for j in orders[i]]), i) for i in range(len(orders))]
#     a.sort()
#     q = deque(a)
#     res = set()
#     while q:
#         x, y, z = q.popleft()
#         for i in range(len(a)):
#             print(x, y, z, a[i])
#             if a[i][2] != z:
#                 tmp = list(y & a[i][1])
#                 if len(tmp) in course:
#                     tmp.sort()
#                     res.add(''.join(tmp))
#     result = list(res)
#     result.sort()
#     return result


# 조합과 Counter 이용
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        tmp = []
        for order in orders:
            comb = combinations(sorted(order), c)
            tmp += comb
        cnt = Counter(tmp)
        if len(cnt) != 0 and max(cnt.values()) != 1:
            answer += [''.join(i) for i in cnt if cnt[i] == max(cnt.values())]
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))