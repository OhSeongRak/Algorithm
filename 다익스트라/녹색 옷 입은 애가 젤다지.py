import sys
from heapq import heappop, heappush, heapify

input = sys.stdin.readline
INF = sys.maxsize


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def dijkstra(N, board):
    distance = [[INF for _ in range(N)] for _ in range(N)]
    pq = []
    distance[0][0] = board[0][0]
    heappush(pq, (board[0][0], 0, 0))

    while pq:
        d, r, c = heappop(pq)

        if distance[r][c] < d:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not in_range(nr, nc):
                continue

            total = d + board[nr][nc]
            if total < distance[nr][nc]:
                distance[nr][nc] = total
                heappush(pq, (total, nr, nc))

    return distance[-1][-1]


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N = int(input())
count = 1
while N != 0:
    board = [list(map(int, input().split())) for _ in range(N)]
    print("Problem {}: {}".format(count, dijkstra(N, board)))
    count += 1
    N = int(input())
