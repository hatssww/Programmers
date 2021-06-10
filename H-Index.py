def solution(citations):
    citations.sort()
    n = len(citations)
    for i in range(n):
        if citations[i] >= n - i:
            return n - i
    return 0


print(solution([1, 5, 7, 2, 8, 10]))