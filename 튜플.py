def solution(s):
    answer = []
    ns = s.lstrip('{').rstrip('}').split('},{')
    data = [i.split(',') for i in ns]
    data.sort(key=len)
    
    for i in data:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer

print(solution(	"{{20,111},{111}}"))