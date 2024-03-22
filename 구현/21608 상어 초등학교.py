import sys

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def solution():
    for numbers in lst:
        st = numbers[0]
        likes = numbers[1:]
        tmp = []

        for r in range(N):
            for c in range(N):
                if board[r][c] != 0:
                    continue

                like, empty = 0, 0
                for dr, dc in drc:
                    nr = r + dr
                    nc = c + dc
                    if not in_range(nr, nc):
                        continue

                    if board[nr][nc] in likes:
                        like += 1
                    if board[nr][nc] == 0:
                        empty += 1

                tmp.append((-like, -empty, r, c))

        tmp.sort()
        board[tmp[0][2]][tmp[0][3]] = st

    lst.sort(key=lambda x: x[0])
    total = 0
    score = [0, 1, 10, 100, 1000]
    for r in range(N):
        for c in range(N):
            likes = lst[board[r][c] - 1][1:]
            happy = 0
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc
                if not in_range(nr, nc):
                    continue
                if board[nr][nc] in likes:
                    happy += 1

            total += score[happy]

    # print(*board, sep='\n')
    return total


N = int(input())
drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
board = [[0] * N for _ in range(N)]
lst = [list(map(int, input().split())) for _ in range(N * N)]
print(solution())
