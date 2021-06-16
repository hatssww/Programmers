# def solution(arr):
#     ans = [0, 0]
#     N = len(arr)

#     def comp(x, y, n):
#         init = arr[x][y]
#         for i in range(x, x + n):
#             for j in range(y, y + n):
#                 if arr[i][j] != init:
#                     nn = n // 2
#                     comp(x, y, nn)
#                     comp(x + nn, y, nn)
#                     comp(x, y + nn, nn)
#                     comp(x + nn, y + nn, nn)
#                     return
#         ans[init] += 1
    
#     comp(0, 0, N)
#     return ans


# numpy 라이브러리 이용
import numpy as np

def solution(arr):
    def comp(a):
        if np.all(a == 0): return np.array([1, 0])
        if np.all(a == 1): return np.array([0, 1])
        n = a.shape[0] // 2
        return comp(a[:n, :n]) + comp(a[:n, n:]) + comp(a[n:, :n]) + comp(a[n:, n:])

    return comp(np.array(arr)).tolist()

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))