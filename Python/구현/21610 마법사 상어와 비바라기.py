import sys

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def solution():
    cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

    for d, s in order:
        moved = []
        for r, c in cloud:
            # 음수가 나오지 않게 하기 위해 N을 더함.
            # 이동 거리를 N으로 나눈 나머지 만큼 이동.
            nr = (N + r + (s % N * drc[d][0])) % N
            nc = (N + c + (s % N * drc[d][1])) % N
            moved.append((nr, nc))
            board[nr][nc] += 1  # 물 양 증가

        for r, c in moved:
            for i in range(4):  # 대각선 물 흡수
                nr = r + dr[i]
                nc = c + dc[i]
                if in_range(nr, nc) and board[nr][nc] > 0:
                    board[r][c] += 1

        cloud = []
        for r in range(N):
            for c in range(N):
                if (r, c) in moved or board[r][c] < 2:
                    continue
                board[r][c] -= 2
                cloud.append((r, c))

    answer = 0
    for r in range(N):
        for c in range(N):
            answer += board[r][c]

    return answer


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order = [list(map(int, input().split())) for _ in range(K)]
drc = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
dr = [-1, -1, 1, 1]
dc = [1, -1, 1, -1]
print(solution())
