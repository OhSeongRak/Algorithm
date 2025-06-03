import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque([(1, 1, 1)])  # 임티 수, 클립 값, 횟수
    # dp = [[0 for _ in range(200001)] for _ in range(200001)]
    # dp[1][1] = 1
    visited = [[False for _ in range(4001)] for _ in range(4001)]
    visited[1][1] = True
    while queue:
        emo, clip, count = queue.popleft()

        if emo <= 0 or clip <= 0 or emo >= 2000 or clip >= 2000:
            continue

        if emo == N:
            return count

        if not visited[emo][emo]:
            visited[emo][emo] = True
            queue.append((emo, emo, count + 1))

        if not visited[emo + clip][clip]:
            visited[emo + clip][clip] = True
            queue.append((emo + clip, clip, count + 1))

        if not visited[emo - 1][clip]:
            visited[emo - 1][clip] = True
            queue.append((emo - 1, clip, count + 1))

    return


N = int(input())
print(bfs())

'''
알아야 될 것. 현재 이모티콘 개수, 클립보드 값
dp[i][j] = N -> i: 임티 수, j: 클립 값, N: 횟수 
'''
