def solution(s):
    if len(s) == 1:
        return 0
    i = 0
    while i <= len(s) - 2:
        print(i, s)
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
            i = 0
        else: i += 1
    if len(s) == 0:
        return 1
    else:
        return 0

print(solution('baabaa'))