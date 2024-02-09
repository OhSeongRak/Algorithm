import sys
from collections import deque

input = sys.stdin.readline


def in_range(l, r, c):
    if 0 <= l < L and 0 <= r < R and 0 <= c < C:
        return True
    return False


def solution():
    start, end = [0, 0, 0], [0, 0, 0]
    dl = [0, 0, 0, 0, 1, -1]
    dr = [-1, 0, 1, 0, 0, 0]
    dc = [0, 1, 0, -1, 0, 0]

    for l in range(L):
        for r in range(R):
            for c in range(C):
                if board[l][r][c] == 'S':
                    start = [l, r, c]
                if board[l][r][c] == 'E':
                    end = [l, r, c]

    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]

    visited[start[0]][start[1]][start[2]] = True
    queue = deque()
    queue.append((start[0], start[1], start[2], 0))

    while queue:
        l, r, c, d = queue.popleft()

        if l == end[0] and r == end[1] and c == end[2]:
            print(f'Escaped in {d} minute(s).')
            return

        for i in range(6):
            nl = l + dl[i]
            nr = r + dr[i]
            nc = c + dc[i]

            if in_range(nl, nr, nc) and not visited[nl][nr][nc] and board[nl][nr][nc] != '#':
                visited[nl][nr][nc] = True

                queue.append((nl, nr, nc, d + 1))

    print("Trapped!")
    return


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    board = []
    for _ in range(L):
        tmp = []
        for _ in range(R):
            tmp.append(list(input().strip()))
        board.append(tmp)
        input()

    solution()

    # for i in range(L):
    #     print(*board[i], sep='\n')
    #     print("==========================")
