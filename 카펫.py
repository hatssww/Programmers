import math

def solution(brown, yellow):
    a = int(math.sqrt(yellow))
    x, y = a, yellow
    while x > 0:
        if y % x == 0:
            y //= x
        else:
            x -= 1
            continue
        if x * 2 + y * 2 + 4 == brown:
            break
        else:
            x -= 1
            y = yellow
    answer = [y + 2, x + 2]
    return answer

print(solution(62, 100))