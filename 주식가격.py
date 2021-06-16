def solution(prices):
    ans = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[j] < prices[i]:
                break
            else:
                ans[i] += 1
    return ans


# 스택을 이용한 풀이
def solution(prices):
    ans = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        if stack:
            while stack and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                ans[past] = i - past
        stack.append([i, prices[i]])
    # 끝까지 가격 떨어지지 않은 것들은 총 길이 - 1 에서 -i 해주면 초 길이가 됨.
    for i, s in stack:
        ans[i] = len(prices) - 1 - i
    return ans


print(solution([1, 2, 3, 2, 3]))