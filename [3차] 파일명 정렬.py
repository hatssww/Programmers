# # 정답은 나오지만 런타임 에러 발생
# def solution(files):
#     ans = []
#     res = []
#     d = {}
#     num = 0
#     for f in files:
#         for i in f:
#             if i.isdigit():
#                 num_idx = f.index(i)
#                 break
#         for i in range(num_idx, len(f)):
#             if f[i].isalpha() or f[i] in [' ', '.', '-']:
#                 tail_idx = i
#                 break
#         f_list = [f[:num_idx].upper(), int(f[num_idx:tail_idx]), f[tail_idx:]]
#         res.append((f_list, num))
#         num += 1
#     res.sort()
#     for i in range(1, len(res)):
#         if res[i-1][0][0] == res[i][0][0] and res[i-1][0][1] == res[i][0][1]:
#             if res[i-1][1] > res[i][1]:
#                 res[i-1], res[i] = res[i], res[i-1]
#     for i, j in res:
#         ans.append(files[j])

#     return ans


# 정규표현식을 이용한 풀이
import re

def solution(files):
    tmp = [re.split(r"([0-9]+)", f) for f in files]
    sort = sorted(tmp, key= lambda x: (x[0].upper(), int(x[1])))
    return ["".join(i) for i in sort]


print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))