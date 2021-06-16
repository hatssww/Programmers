# 지나간 길 스택으로 표시
def solution(dirs):
    x, y = 5, 5
    cnt = 0
    stack = []
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            nx = x - 1
            ny = y
        elif dirs[i] == 'D':
            nx = x + 1
            ny = y
        elif dirs[i] == 'L':
            nx = x
            ny = y - 1
        elif dirs[i] == 'R':
            nx = x
            ny = y + 1
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            if [(x, y), (nx, ny)] not in stack:
                stack.append([(x, y), (nx, ny)])
                stack.append([(nx, ny), (x, y)])
                cnt += 1
            x, y = nx, ny
        
    return cnt


# 지나간 길 집합으로 표시
def solution(dirs):
    s = set()
    d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x, y, nx, ny))
            s.add((nx, ny, x, y))
            x, y = nx, ny
    return len(s) // 2


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))