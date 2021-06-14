from collections import deque

def solution(cacheSize, cities):
    time = 0
    q = deque()
    if cacheSize == 0:
        return len(cities) * 5
    for i in cities:
        i = i.upper()
        if not q:
            q.append(i)
            time += 5
        elif len(q) < cacheSize and i not in q:
            q.append(i)
            time += 5
        elif len(q) == cacheSize and i not in q:
            q.popleft()
            q.append(i)
            time += 5
        elif len(q) <= cacheSize and i in q:
            q.remove(i)
            q.append(i)
            time += 1
    return time


# deque의 maxlen 이용
from collections import deque

def solution(cacheSize, cities):
    time = 0
    q = deque(maxlen=cacheSize)
    for i in cities:
        i = i.upper()
        if i in q:
            q.remove(i)
            q.append(i)
            time += 1
        else:
            q.append(i)
            time += 5
    return time


print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))