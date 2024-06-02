import sys

input = sys.stdin.readline


def solution():
    for r in range(1, N):
        for c in range(1, M):
            if board[r][c] == 0:
                continue
            board[r][c] += min(board[r - 1][c], board[r][c - 1], board[r - 1][c - 1])

    answer = 0
    for r in range(N):
        for c in range(M):
            answer = max(answer, board[r][c])

    return answer


while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    board = [list(map(int, input().split())) for _ in range(N)]
    print(solution())
