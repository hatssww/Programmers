from collections import deque
def is_true(stack):
    tmp = []
    for i in stack:
        if i == "(":
            tmp.append(i)
        if i == ")":
            if tmp and tmp[-1] == "(":
                tmp.pop()
            else:
                tmp.append(i)
    if not tmp:
        return True
    else: return False


def convert(u):
    u.pop(0)
    u.pop()
    if not u:
        return ""
    res = ""
    for i in range(len(u)):
        if u[i] == "(":
            res += ")"
        elif u[i] == ")":
            res += "("
    return res


def solution(p):
    answer = ''
    w = deque()
    for i in p:
        w.append(i)   
    stack = []
    u = ""
    v = ""
    while w:
        x = w.popleft()
        stack.append(x)

        if is_true(stack):
            for i in stack:
                answer += i
            stack = []

        else:
            if stack.count("(") == stack.count(")"):
                for _ in range(len(w)):
                    i = w.popleft()
                    v += i
                tmp = "(" + solution(v) + ")"
                answer += tmp + convert(stack)
                stack = []

    return answer

print(solution(")("))


# is_true()는 이렇게도 표현할 수 있음
def is_true(stack):
    tmp = 0
    for i in stack:
        if i == '(':
            tmp += 1
        else:
            tmp -= 1
            if tmp < 0:
                return False
    return tmp == 0