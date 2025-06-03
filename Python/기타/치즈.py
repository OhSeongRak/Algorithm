import sys
from collections import deque
input = sys.stdin.readline


def check_out_air():
    queue = deque([(0, 0)])
    visited[0][0] = True
    board[0][0] = -1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
        
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visited[nr][nc] or board[nr][nc] == 1:
                continue
        
            visited[nr][nc] = True
            board[nr][nc] = -1
            queue.append((nr, nc))

def check_remove_cheese():
    for r in range(N):
        for c in range(M):
            if board[r][c] != 1:
                continue
            cnt = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
            
                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue
                if board[nr][nc] == -1:
                    cnt += 1
            
            if cnt >= 2:
                melt_cheese.add((r, c))
    return

def solution():
    cnt = 0
    while True:
        isRemain = False
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    isRemain = True
                    break
        
        if not isRemain:
            return cnt
        cnt += 1

        check_out_air()
        check_remove_cheese()
        for r, c in melt_cheese:
            board[r][c] = 0

        for i in range(N):
            for j in range(M):
                visited[i][j] = False
        

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
melt_cheese = set()
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
print(solution())
# print(*board, sep='\n')
# 외부 공기인 부분을 -1로 초기화
# 반복문을 통해 치즈 제거
# 치즈일 경우, 해당