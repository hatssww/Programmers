# # 뭔가 이동시키는 개념은 맞았는데 좀 효율적이지 못함, 옮기는 과정에 오류도 있음.
# from collections import deque
# def solution(rows, columns, queries):
#     answer = []
#     arr = [[] for i in range(rows)]
#     num = 1
#     for i in range(rows):
#         for j in range(columns):
#             arr[i].append(num)
#             num += 1
    
#     for q in queries:
#         x1, y1 = q[0] - 1, q[1] - 1
#         x2, y2 = q[2] - 1, q[3] - 1
#         tmp1 = 0
#         tmp2 = arr[x1][y1]
#         mini = arr[x1][y1]
#         x, y = x1, y1
#         while True:    
#             if x == x1:
#                 x = x
#                 y = y + 1
#                 if y <= y2:
#                     tmp1 = arr[x][y]
#                     arr[x][y] = tmp2
#                     tmp2 = tmp1
#                     mini = min(mini, tmp2)
#                 if y == y2:
#                     x += 1
#             elif x == x2 + 1:
#                 x = x
#                 y = y - 1
#                 if y >= y2:
#                     tmp1 = arr[x][y]
#                     arr[x][y] = tmp2
#                     tmp2 = tmp1
#                     mini = min(mini, tmp2)
#                 if y == y1:
#                     x -= 1
#             else:
#                 x = x
#                 y = y
#                 if x1 <= x <= x2:
#                     tmp1 = arr[x][y]
#                     arr[x][y] = tmp2
#                     tmp2 = tmp1
#                     mini = min(mini, tmp2)
#                     if y == y2:
#                         x += 1
#                     elif y == y1:
#                         x -= 1
#             if x == x1 and y == y1:
#                 break
#         answer.append(mini)
#     return answer


# 깔끔한 풀이
def solution(rows, columns, queries):
    answer = []
    arr = [[] for _ in range(rows)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            arr[i-1].append((i-1) * columns + j)
    
    for x1, y1, x2, y2 in queries:
        temp = arr[x1-1][y2-1]
        min_value = 10001
    
        # 위쪽 테두리 밀어서 업데이트 →
        min_value = min(min(arr[x1-1][y1-1:y2-1]), min_value)
        arr[x1-1][y1:y2] = arr[x1-1][y1-1:y2-1]

        # 왼쪽 테두리 밀어서 업데이트 ↑
        for i in range(x1, x2):
            min_value = min(arr[i][y1-1], min_value)
            arr[i-1][y1-1] = arr[i][y1-1]
        
        # 아래쪽 테두리 밀어서 업데이트 ←
        min_value = min(min(arr[x2-1][y1:y2]), min_value)
        arr[x2-1][y1-1:y2-1] = arr[x2-1][y1:y2]

        # 오른쪽 테두리 밀어서 업데이트 ↓
        for i in range(x2-2, x1-2, -1):
            min_value = min(arr[i][y2-1], min_value)
            arr[i+1][y2-1] = arr[i][y2-1]
        
        arr[x1][y2-1] = temp  # 밀려서 사라진 값 저장해 둔 값으로 지정
        min_value = min(min_value, temp)

        answer.append(min_value)
    
    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))