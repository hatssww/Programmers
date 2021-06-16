# 답은 맞지만 시간초과
def make_dp(n):
    INF = 1000000001
    dp = [0, 1] + [INF] * (n - 1)
    for i in range(2, n+1):
        if dp[i] == INF:
            if i % 2 == 0:
                dp[i] = min(dp[i-1] + 1, dp[i//2])
            if i % 2 == 1:
                dp[i] = dp[i-1] + 1
            
            j = i * 2
            while j <= n:
                dp[j] = dp[i]
                j *= 2
    return dp

def solution(n):
    dp = make_dp(n)
    return dp[n]


# 그냥 간단히 2로 나눈 나머지들을 더해주면 됨(점프한 횟수)
def solution(n):
    ans = 0
    while n > 0:
        q, r = divmod(n, 2)
        n = q
        ans += r
    return ans


# 더 간단히 이진법으로 해결 가능
def solution(n):
    return bin(n).count('1')


print(solution(5))