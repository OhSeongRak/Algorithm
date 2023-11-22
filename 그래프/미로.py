import sys
from collections import deque

input = sys.stdin.readline


def printAns(sr, sc, r, c):
    while r != sr or c != sc:
        prev_r, prev_c = last[r][c]
        board[prev_r][prev_c] = "."
        r, c = prev_r, prev_c

    for i in range(N):
        for j in range(M):
            print(board[i][j], end="")
        print()

    return


def bfs():
    # 길을 다 @로 해놓고 왔던 경로만 .으로 바꿀 예정
    for i in range(N):
        for j in range(M):
            if board[i][j] == ".":
                board[i][j] = "@"

    # 시작, 끝 점을 찾기 위한 반복문
    sr, sc, er, ec = -1, -1, -1, -1
    for i in range(N):
        for j in range(M):
            # 가장자리만 보기위해서
            if 0 < i < N - 1 and 0 < j < M - 1:
                continue
            if board[i][j] == "@":
                if sr == -1 and sc == -1:
                    sr, sc = i, j
                else:
                    er, ec = i, j

    # 시작 끝 점은 맘 편히 .으로 바꿔주자
    board[sr][sc], board[er][ec] = ".", "."
    queue = deque([(sr, sc)])
    visited[sr][sc] = True

    while queue:
        r, c = queue.popleft()

        if r == er and c == ec:
            printAns(sr, sc, r, c)  # 출력해주자
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if visited[nr][nc] == True or board[nr][nc] == "+":
                continue

            queue.append((nr, nc))
            last[nr][nc] = (r, c)  # 전에 방문한 점을 담자
            visited[nr][nc] = True

    return


N, M = map(int, input().split())
visited = [[False for _ in range(M)] for _ in range(N)]  # 방문처리
# last[r][c] := (r, c)를 방문하기 직전에 왔던 점
last = [[(-1, -1) for _ in range(M)] for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
board = [list(input().rstrip()) for _ in range(N)]
bfs()
