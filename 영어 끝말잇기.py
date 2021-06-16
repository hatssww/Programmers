# def solution(n, words):
#     cnt = 0
#     idx = 0
#     before = [words[0]]
#     while idx < len(words):
#         cnt += 1
#         for i in range(1, n + 1):
#             if idx != 0 and (words[idx] in before or words[idx-1][-1] != words[idx][0]):
#                 return [i, cnt]
#             else:           
#                 before.append(words[idx])
#                 idx += 1
#                 if idx >= len(words):
#                     break
#     return [0, 0]


# 더 간결한 답 구하는 방법
def solution(n, words):
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return [i % n + 1, i // n + 1]    
    return [0, 0]

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))