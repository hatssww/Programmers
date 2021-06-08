def solution(n):
    answer = ''
    num = ['4', '1', '2']
    while n != 0:
        answer = num[n % 3] + answer
        if n % 3 == 0:
            n = n//3 - 1
        else:
            n //= 3

    return answer

print(solution(13))