import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def dfs(p):
    visited.add(p)

    for c in graph[p]:  # c: 자식, p: 부모
        if c in visited:
            continue
        dfs(c)
        dp[p][0] += dp[c][1]  # 부모가 얼리어답터가 아니면, 자식은 무조건 얼리어답터임
        dp[p][1] += min(dp[c][0], dp[c][1])  # 부모가 얼리어답터라면, 자식은 둘 중 작은 값

    return


N = int(input())
graph = defaultdict(list)

for _ in range(N - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dp = [[0, 1] for _ in range(N + 1)]
visited = set()
dfs(1)
# print(*dp, sep='\n')
print(min(dp[1][0], dp[1][1]))

'''
dp[i][0] = i가 root이고, 얼리어답터가 아닌 경우 트리의 최적해
dp[i][1] = i가 root이고, 얼리어답터인 경우 트리의 최적해
'''
