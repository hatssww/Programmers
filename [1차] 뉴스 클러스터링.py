from collections import Counter

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    a = [str1[i:i + 2] for i in range(len(str1) - 1) if str1[i].isalpha() and str1[i + 1].isalpha()]
    b = [str2[i:i + 2] for i in range(len(str2) - 1) if str2[i].isalpha() and str2[i + 1].isalpha()]
    
    a_count = Counter(a)
    b_count = Counter(b)

    inter = a_count & b_count
    union = a_count | b_count

    inter_sum = sum(inter.values())
    union_sum = sum(union.values())
    
    if union_sum == 0:
        return 65536

    answer = inter_sum / union_sum
    return int(answer * 65536)

print(solution("FRANCE", "french"))
print(solution("aa1+aa2", "AAAA12"))


# 이것도 맞았는데 위처럼 그냥 카운터 값으로 합집합 교집합 연산 가능함
# from collections import Counter

# def solution(str1, str2):
#     str1 = str1.upper()
#     str2 = str2.upper()
#     a = ["".join([str1[i], str1[i + 1]]) for i in range(len(str1) - 1) if str1[i].isalpha() and str1[i + 1].isalpha()]
#     b = ["".join([str2[i], str2[i + 1]]) for i in range(len(str2) - 1) if str2[i].isalpha() and str2[i + 1].isalpha()]
    
#     inter = set(a) & set(b)
#     union = set(a) | set(b)

#     if len(union) == 0:
#         return 65536

#     inter_sum = sum([min(a.count(i), b.count(i)) for i in inter])
#     union_sum = sum([max(a.count(i), b.count(i)) for i in union])

#     answer = inter_sum / union_sum
#     return int(answer * 65536)

# print(solution("FRANCE", "french"))
# print(solution("aa1+aa2", "AAAA12"))