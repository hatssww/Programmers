def solution(numbers):
    ans = []
    for i in numbers:
        ni = list('0' + bin(i)[2:])
        idx = ''.join(ni).rfind('0')
        ni[idx] = '1'

        if i % 2 == 1:
            ni[idx + 1] = '0'
        
        ans.append(int(''.join(ni), 2))
                    
    return ans

print(solution([2, 7, 9]))