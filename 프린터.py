from collections import deque

def solution(priorities, location):
    prio = [(v, i) for i, v in enumerate(priorities)]
    cnt = 0
    q = deque(prio)
    while q:
        x, y = q.popleft()
        if q and x < max(q)[0]:  # q가 비었으면 바로 종료시켜주기
            q.append((x, y))
        else:
            cnt += 1
            if y == location:
                break
    return cnt

print(solution([1, 1, 1, 1, 1], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))