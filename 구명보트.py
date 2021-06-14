def solution(people, limit):
    n = len(people)
    people.sort(reverse=True)
    start, end = 0, n-1
    while start < end:
        if people[start] + people[end] <= limit:
            end -= 1
            n -= 1
        start += 1
    return n

print(solution([70, 50, 80, 50], 100))