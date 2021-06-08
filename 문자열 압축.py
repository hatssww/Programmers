from collections import deque


def solution(s):
    result = 1001
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)):
        t = s
        q = deque()
        res = ""
        cnt = 0
        while len(t) != 0:
            if not q:
                q.append(t[:i])
                t = t[i:]
                continue
            if t[:i] in q and t[:i] == q[-1]:
                q.append(t[:i])
                t = t[i:]
            if t[:i] not in q:
                tmp = q[0]
                while q:
                    q.popleft()
                    cnt += 1
                if cnt > 1:
                    res = res + str(cnt) + tmp
                    cnt = 0
                else:
                    res = res + tmp
                    cnt = 0
                q.append(t[:i])
                t = t[i:]
        res = res + q[0]
        result = min(result, len(res))

    return result


print(solution('abcabcabcabcdededededede'))