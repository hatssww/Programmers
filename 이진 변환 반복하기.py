def solution(s):
    cnt, sum = 0, 0
    while s != '1':
        cnt += 1
        zero = s.count('0')
        sum += zero
        num = len(s) - zero
        s = bin(num)[2:]
    return [cnt, sum]


print(solution("1111111"))