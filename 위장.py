from itertools import combinations

def solution(clothes):
    kind = {}
    for i, v in clothes:
        kind[v] = kind.get(v, []) + [i]
    cnt = [len(i) for i in kind.values()]
    ans = 1
    for i in cnt:
        ans *= (i + 1)

    return ans - 1


# reduce함수 이용
from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for item, kind in clothes])
    ans = reduce(lambda x, y: x * (y + 1), cnt.values(), 1)
    return ans - 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))