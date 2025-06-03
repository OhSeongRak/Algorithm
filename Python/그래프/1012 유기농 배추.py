import sys
from collections import deque

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def solution():
    def bfs(r, c):
        nonlocal visited

        queue = deque()
        queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc

                if not in_range(nr, nc) or visited[nr][nc] or board[nr][nc] == 0:
                    continue

                queue.append((nr, nc))
                visited[nr][nc] = True

        return

    drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * C for _ in range(R)]
    ans = 0
    for r in range(R):
        for c in range(C):
            if not visited[r][c] and board[r][c] == 1:
                bfs(r, c)
                ans += 1

    return ans


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        C, R, K = map(int, input().split())
        board = [[0] * C for _ in range(R)]
        for _ in range(K):
            c, r = map(int, input().split())
            board[r][c] = 1

        # print(*board, sep='\n')
        print(solution())
