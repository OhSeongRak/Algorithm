import sys

from collections import deque

input = sys.stdin.readline


def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()

        for dr, dc in drc:
            nr = (r + dr) % R
            nc = (c + dc) % C
            if board[nr][nc] == 1 or visited[nr][nc]:
                continue
            queue.append((nr, nc))
            visited[nr][nc] = True

    return


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
# print(*board, sep='\n')
visited = [[False] * C for _ in range(R)]
drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0

for r in range(R):
    for c in range(C):
        if board[r][c] == 1 or visited[r][c]:
            continue
        bfs(r, c)
        answer += 1

print(answer)
