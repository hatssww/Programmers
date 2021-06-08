def when(progresses, speeds):
    if (100 - progresses) % speeds == 0:
        return (100 - progresses) // speeds
    else:
        return (100 - progresses) // speeds + 1


def solution(progresses, speeds):
    n = len(progresses)
    finish = [0] * n

    for i in range(n):
        day = when(progresses[i], speeds[i])
        finish[i] = day
    
    num = finish[0]
    cnt = 1
    res = []
    for i in range(1, n):
        if finish[i] > num:
            res.append(cnt)
            num = finish[i]
            cnt = 1
        else:
            cnt += 1
    res.append(cnt)
    return res


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))