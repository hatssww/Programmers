def solution(record):
    answer = []
    state = {}
    for r in record:
        rec = list(map(str, r.split()))
        if rec[0] == 'Enter' or rec[0] == 'Change':
            state[rec[1]] = rec[2]
    for r in record:
        if r.split()[0] == 'Enter':
            answer.append(f"{state.get(r.split()[1])}님이 들어왔습니다.")
        if r.split()[0] == 'Leave':
            answer.append(f"{state.get(r.split()[1])}님이 나갔습니다.")
    
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))