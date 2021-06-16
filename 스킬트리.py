from collections import deque

def solution(skill, skill_trees):
    ans = 0
    for tree in skill_trees:
        skill_list = deque(skill)
        for s in tree:
            if s in skill:
                if s != skill_list.popleft():
                    break
        else: ans += 1
    return ans


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))