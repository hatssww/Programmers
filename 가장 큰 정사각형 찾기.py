from itertools import chain  # 첫 번째 이터러블에서 소진될 때까지 요소를 반환한 다음 이터러블로 넘어가고, 이런 식으로 iterables의 모든 이터러블이 소진될 때까지 진행하는 이터레이터를 만듦.

def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    
    return max(chain(*board))**2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))