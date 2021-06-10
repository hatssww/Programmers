def is_true(s):
    tmp = []
    for i in s:
        if i in "({[":
            tmp.append(i)
        if i in ")}]":
            if tmp and tmp[-1] in "({[":
                if i == ")" and tmp[-1] == "(": tmp.pop()
                if i == "}" and tmp[-1] == "{": tmp.pop()
                if i == "]" and tmp[-1] == "[": tmp.pop()
            else:
                tmp.append(i)
    
    return True if not tmp else False


def solution(s):
    answer = 0
    for i in range(len(s)):
        if is_true(s[i:] + s[:i]):
            answer += 1

    return answer

print(solution("[](){}"))
"}]()[{"
"[)(]"
"}}}"