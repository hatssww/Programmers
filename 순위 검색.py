# # 정확성은 만점, 효율성은 0점
# def is_true(i, cond):
#     cnt = 0
#     for j in range(4):
#         if cond[j] == "-" or cond[j] == i[j]:
#             cnt += 1
#     return True if cnt == 4 and int(cond[4]) <= int(i[4]) else False


# def solution(info, query):
#     info_list = [i.split(" ") for i in info]
#     res = []
#     for q in query:
#         cond = [i for i in q.split(" ") if i != 'and']
#         num = 0
#         for i in info_list:
#             if is_true(i, cond):
#                 num += 1
#         res.append(num)

#     return res


# 효율성 개선
# 이미 가진 데이터에서 가능한 모든 조건을 미리 구하고, 사람들의 점수를 그 해당하는 조건들에 모두 입력해서 딕셔너리 만듬.
# 쿼리에 있는 조건에 해당하는 딕셔너리 키의 값들의 개수 - 쿼리 조건에 해당하는 점수가 들어갈 위치를 bisect_left(이진분할알고리즘)를 통해 찾아서 그 인덱스 값을 빼줌.
# 결과는 전체 - 조건보다 미만인 점수 개수(인덱스값) = 조건에 해당하는 점수 개수(사람 수)

from itertools import combinations
from bisect import bisect_left

def make_all_cases(s):
    cases = []
    for i in range(5):
        for comb in combinations(range(4), i):
            case = ''
            for j in range(4):
                if j not in comb:
                    case += s[j]
                else: case += '-'
            cases.append(case)
    return cases

def solution(info, query):
    res = []
    all_cases = {}
    for i in info:
        i_list = i.split()
        cases = make_all_cases(i_list)
        for c in cases:
            if c not in all_cases.keys():
                all_cases[c] = [int(i_list[4])]
            else:
                all_cases[c].append(int(i_list[4]))


    for k in all_cases.keys():
        all_cases[k].sort()
    
    for q in query:
        q_list = q.split()
        cond = q_list[0] + q_list[2] + q_list[4] + q_list[6]
        if cond in all_cases.keys():
            res.append(len(all_cases[cond]) - bisect_left(all_cases[cond], int(q_list[7]), lo=0, hi=len(all_cases[cond])))
        else:
            res.append(0)

    return res


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))