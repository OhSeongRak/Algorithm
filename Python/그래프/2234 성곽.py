import sys

from collections import deque

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def solution1(r, c, num):
    queue = deque()
    queue.append((r, c))
    area[r][c] = num
    count = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + d[i]
            nc = c + d[i + 1]

            if board[r][c] & (2 ** i) == (2 ** i):  # 벽이라면
                continue

            if not in_range(nr, nc) or area[nr][nc] != 0:  # 범위 밖이나, 방문했다면
                continue

            queue.append((nr, nc))
            area[nr][nc] = num
            count += 1

    size.append(count)
    return


def solution3():
    for r in range(R):
        for c in range(C):
            for i in range(4):
                nr = r + d[i]
                nc = c + d[i + 1]
                if not in_range(nr, nc):
                    continue

                if board[r][c] & (2 ** i) == (2 ** i):  # 벽이라면
                    aside[area[r][c]].add(area[nr][nc])

    return


d = [0, -1, 0, 1, 0]
C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
area = [[0] * C for _ in range(R)]
size = [0]

count = 1
for r in range(R):
    for c in range(C):
        if area[r][c] == 0:
            solution1(r, c, count)
            count += 1

aside = [set() for _ in range(len(size))]
solution3()

print(len(size) - 1)
print(max(size))
answer3 = 0
for i in range(1, len(size)):
    for k in aside[i]:
        if i == k:
            continue
        answer3 = max(answer3, size[i] + size[k])
print(answer3)
