import sys

input = sys.stdin.readline


def solution():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if floyd[i][j] == 0:
                    floyd[i][j] = floyd[i][k] * floyd[k][j]

    count = 0
    for i in range(1, N + 1):
        tmp = 0
        for j in range(1, N + 1):
            tmp += floyd[i][j] | floyd[j][i]
        if tmp == N - 1:
            count += 1

    return count


N, M = map(int, input().split())
floyd = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    floyd[s][e] = 1

print(solution())
