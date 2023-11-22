import sys
input = sys.stdin.readline


def recur(pos, total):
    global answer
    r, c = pos // M, pos % M
    
    if pos == N*M:
        answer = max(answer, total)
        return

    if visited[r][c]: # 이미 현재 위치에 방문했다면 진행
        recur(pos + 1, total)
        return
    
    # 가로 (1개, 2개, 3개, 4개)
    tmp = 0
    reset_c = c # 가로로 어디까지 갔는지 체크
    for i in range(c, M):
        if not visited[r][i]:
            visited[r][i] = True
            tmp = tmp * 10 + board[r][i]
            recur(pos+1, total + tmp)
            reset_c = i # 가로로 어디까지 갔는지 체크
        else:
            break
    
    # 가로는 c ~ reset_c까지 확인했음. => reset_c까지 다시 방문 초기화
    for i in range(c+1, reset_c+1):
        visited[r][i]= False

    # 세로 (2개, 3개, 4개)
    tmp = board[r][c]
    reset_r = r
    for i in range(r+1, N):
        if not visited[i][c]:
            visited[i][c] = True
            tmp = tmp * 10 + board[i][c]
            recur(pos+1, total + tmp)
            reset_r = i
        else:
            break
    
    # 세로는 r ~ reset_r까지 확인했음. => reset_r까지 다시 방문 초기화
    for i in range(r, reset_r+1):
        visited[i][c] = False

    return

N, M = map(int, input().split())
answer = 0
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
recur(0, 0)
print(answer)