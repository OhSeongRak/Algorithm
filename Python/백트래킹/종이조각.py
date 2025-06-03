import sys
input = sys.stdin.readline

# (N-1) x (N-1) 배열 2개를 만듦
# 오른쪽 벽을 없앤 배열 표시
# 아래쪽 벽을 없애 배열 표시
# N x N 방문배열 표시
# 오른쪽 싹다 더하고, 아래쪽 싹다 더하고
# 방문배열 돌면서 처리
def solve():
    visited = [[False] * M for _ in range(N)]
    global answer
    total = 0

    for i in range(N):
        st = ""
        for j in range(M):
            if right[i][j] == True:
                st += board[i][j]
                visited[i][j] = True
            else:
                if len(st) != 0:
                    total += int(st + board[i][j])
                    visited[i][j] = True
                    st = ""
    
    for i in range(M):
        st = ""
        for j in range(N):
            if bottom[j][i] == True:
                st += board[j][i]
                visited[j][i] = True
            else:
                if len(st) != 0:
                    total += int(st + board[j][i])
                    visited[j][i] = True
                    st = ""

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                total += int(board[i][j])

    answer = max(total, answer)


def reset(lst):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            lst[i][j] = False


def solution():
    # 오르쪽 벽의 부분집합 (0, 1, 2, 3, 4, 5... 12)
    # => (0, 0), (0, 1), (0, 2) .. (3, 2)
    for i in range(1 << N * (M-1)):
        for j in range(N * (M-1)):
            if i & (1 << j):
                right[j // (M-1)][j % (M-1)] = True
            
            # 아래쪽 벽의 부분집합
            for k in range(1 << (N-1) * M):
                for l in range((N-1) * M):
                    # 겹치면 안됨
                    if k & (1 << l) and not right[l // M][l % M] and not right[l // M][l % M + 1]:
                        bottom[l // M][l % M] = True
                
                solve()
                reset(bottom)
        
        reset(right)

    return

answer = 0
N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
right = [[False] * (M+1) for _ in range(N)]
bottom = [[False] * M for _ in range(N)]
solution()
print(answer)
# 1 1 1 1
# 1 1 2
# 1 2 1
# 1 3
# 2 1 1
# 2 2
# 3 1
# 4