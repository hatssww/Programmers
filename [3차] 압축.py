def solution(msg):
    d = {}
    for i in range(1, 27):
        d[chr(64 + i)] = i

    w, i = 0, 0
    ans = []

    while True:
        i += 1
        if i == len(msg):
            ans.append(d[msg[w:i]])
            break
        if msg[w:i+1] not in d:
            d[msg[w:i+1]] = len(d) + 1
            ans.append(d[msg[w:i]])
            w = i

    return ans


print(solution('ABABABABABABABAB'))