"""
정수 1은 익은 토마토,
정수 0 은 익지 않은 토마토,
정수 -1은 토마토가 들어있지 않은 칸
"""

import sys
from collections import deque

input = sys.stdin.readline


def in_range(h, m, n):
    if 0 <= h < H and 0 <= m < M and 0 <= n < N:
        return True
    return False


def solution():
    day = 0
    queue = deque()
    visited = [[[False for _ in range(N)] for _ in range(M)] for _ in range(H)]

    for h in range(H):
        for m in range(M):
            for n in range(N):
                if board[h][m][n] == 1:  # 익은 토마토의 위치 저장
                    queue.append((h, m, n, 0))
                    visited[h][m][n] = True

    while queue:
        h, m, n, day = queue.popleft()

        for dh, dm, dn in dhnm:
            nh = h + dh
            nm = m + dm
            nn = n + dn

            if not in_range(nh, nm, nn) or visited[nh][nm][nn]:
                continue

            if board[nh][nm][nn] == 0:
                board[nh][nm][nn] = 1
                visited[nh][nm][nn] = True
                queue.append((nh, nm, nn, day + 1))

    for h in range(H):
        for m in range(M):
            for n in range(N):
                if board[h][m][n] == 0:  # 다 체크하고도 안익은 토마토가 있다면
                    return -1

    return day


if __name__ == "__main__":
    N, M, H = map(int, input().split())
    board = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]
    dhnm = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    print(solution())
