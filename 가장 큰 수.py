def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key= lambda x: x * 3, reverse=True)
    answer = str(int(''.join(num)))
    return answer


data = [3, 30, 51, 104, 0, 9]
data2 = [383, 38]
print(solution(data))
print(solution(data2))