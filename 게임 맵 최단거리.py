from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dp = [[0] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([[0, 0]])
    dp[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] != 0 and not dp[nx][ny]:
                    dp[nx][ny] = dp[x][y] + 1
                    q.append([nx, ny])

    if not dp[n-1][m-1]:
        return -1
    else: return dp[n-1][m-1]


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))