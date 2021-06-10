def solution(name):
    updown = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    idx = 0
    ans = 0
    print(updown)
    while True:
        print(updown)

        ans += updown[idx]
        updown[idx] = 0
        if sum(updown) == 0:  # 모두 입력했으면
            return ans
        
        left, right = 1, 1
        while updown[idx - left] == 0:
            left += 1
        while updown[idx + right] == 0:
            right += 1
        
        ans += left if left < right else right
        idx += -left if left < right else right

print(solution("JEROEN"))
print(solution("ABBAAAAAB"))