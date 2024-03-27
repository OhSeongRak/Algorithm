import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def recur(cur, w):
    dp[cur] = w + praise[cur]
    for child in graph[cur]:
        recur(child, dp[cur])

    return


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
emp = list(map(int, input().split()))
for i in range(1, N):
    graph[emp[i]].append(i + 1)

praise = [0] * (N + 1)
for _ in range(M):
    num, w = map(int, input().split())
    praise[num] += w

dp = [0] * (N + 1)
recur(1, 0)

print(*dp[1:])
