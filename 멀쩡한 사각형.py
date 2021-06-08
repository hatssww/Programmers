# # 삼각형에서 안잘린 부분 개수 세는 방법
# from math import ceil

# def solution(w, h):
#     answer = 0
#     if h / w == 1:
#         return w * h - w
#     elif w == 1 or h == 1:
#         return 0 
#     for x in range(1, w):
#         cut = ceil((h / w) * x)
#         answer += h - cut

#     return answer * 2

# print(solution(8, 12))
# print(solution(5, 5))


# 최대공약수 이용
# def gcd(a, b): return b if (a == 0) else gcd(b%a, a)
from math import gcd

def solution(w, h):
    return w * h - w - h + gcd(w, h)

print(solution(8, 12))
print(solution(5, 5))