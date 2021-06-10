from itertools import combinations

def solution(relation):
    cand = []
    row, col = len(relation), len(relation[0])
    a = [i for i in range(col)]
    comb = []
    for i in range(1, col + 1):
        comb += list(set(i) for i in combinations(a, i))

    for c in comb:
        valid = set()
        for i in range(row):
            tmp = ""
            for j in c:
                tmp += relation[i][j]
            valid.add(tmp)
        if len(valid) == row:
            cand.append(c)

    not_min = set()
    for i in cand:
        for idx, value in enumerate(cand):
            if i.issubset(value) and i != value:
                not_min.add(idx)
    
    answer = len(cand) - len(not_min)
    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))