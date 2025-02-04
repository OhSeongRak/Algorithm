import sys

input = sys.stdin.readline


def recur(pos, cnt, total):
    global answer

    if cnt == 3:
        answer = min(answer, total)
        return

    if pos == (N - 2) * (N - 2):
        return

    r = 1 + pos // (N - 2)
    c = 1 + pos % (N - 2)

    if not visited[r][c] and not visited[r + 1][c] and not visited[r][c + 1] and not visited[r - 1][c] and not \
            visited[r][c - 1]:
        visited[r][c] = True
        visited[r + 1][c] = True
        visited[r][c + 1] = True
        visited[r - 1][c] = True
        visited[r][c - 1] = True
        recur(pos + 1, cnt + 1,
              total + board[r][c] + board[r + 1][c] + board[r][c + 1] + board[r - 1][c] + board[r][c - 1])
        visited[r][c] = False
        visited[r + 1][c] = False
        visited[r][c + 1] = False
        visited[r - 1][c] = False
        visited[r][c - 1] = False

    recur(pos + 1, cnt, total)
    return


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    answer = 3000
    recur(0, 0, 0)
    print(answer)
