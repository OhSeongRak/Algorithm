import sys

input = sys.stdin.readline


def check(r, c, dr, dc):
    global answer

    board[r][c], board[r + dr][c + dc] = board[r + dr][c + dc], board[r][c]

    for i in range(N):
        for j in range(N):
            cnt = 1
            for k in range(i + 1, N):
                if board[i][j] != board[k][j]:
                    break
                cnt += 1
            answer = max(answer, cnt)

            cnt = 1
            for k in range(j + 1, N):
                if board[i][j] != board[i][k]:
                    break
                cnt += 1
            answer = max(answer, cnt)

    board[r][c], board[r + dr][c + dc] = board[r + dr][c + dc], board[r][c]

    return


def solution():
    for r in range(N):
        for c in range(N):
            if r + 1 < N:
                check(r, c, 1, 0)
            if c + 1 < N:
                check(r, c, 0, 1)

    return


if __name__ == "__main__":
    N = int(input())
    answer = 1
    board = [list(input().strip()) for _ in range(N)]
    solution()
    print(answer)
