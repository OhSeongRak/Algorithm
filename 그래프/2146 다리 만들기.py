import sys
from collections import deque

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def add_island(number, r, c):
    queue = deque([(r, c)])
    border = set()
    visited[r][c] = True
    board[r][c] = number

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not in_range(nr, nc) or visited[nr][nc]:  # 범위 밖이거나, 이미 방문했다면
                continue

            if board[nr][nc] == 0:  # 주위에 바다가 있다면
                border.add((r, c))
                continue

            queue.append((nr, nc))
            board[nr][nc] = number
            visited[nr][nc] = True

    island.append(border)
    return


def bfs(num, r, c):
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque([(r, c, 0)])
    visited[r][c] = True

    while queue:
        r, c, d = queue.popleft()

        if board[r][c] != 0 and board[r][c] != num:  # 육지고, 나와 이어진 육지가 아니라면
            return d - 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not in_range(nr, nc) or visited[nr][nc]:  # 범위 밖이거나, 이미 방문했다면
                continue

            queue.append((nr, nc, d + 1))
            visited[nr][nc] = True

    return


def solution():
    answer = 200
    number = 1
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and not visited[i][j]:
                add_island(number, i, j)
                number += 1

    num = 1
    for border in island:
        for r, c in border:
            answer = min(answer, bfs(num, r, c))
        num += 1

    return answer


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
island = []

print(solution())
