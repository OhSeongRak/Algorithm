import sys
from collections import deque

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    size = 1

    while queue:
        r, c = queue.popleft()

        for dr, dc in drc:
            nr = r + dr
            nc = c + dc

            if in_range(nr, nc) and not visited[nr][nc] and board[nr][nc] == 1:
                size += 1
                visited[nr][nc] = True
                queue.append((nr, nc))

    return size


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
count = 0
max_size = 0
for r in range(R):
    for c in range(C):
        if board[r][c] == 1 and not visited[r][c]:
            visited[r][c] = True
            max_size = max(max_size, bfs(r, c))
            count += 1

print(count)
print(max_size)
