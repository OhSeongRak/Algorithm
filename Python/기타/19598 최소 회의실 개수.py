import sys

from heapq import heappop, heappush

input = sys.stdin.readline


def solution():
    pq = [lst[0][1]]

    for s, e in lst[1:]:
        if s >= pq[0]:  # 한 회의실로 가능할 때
            heappop(pq)
        heappush(pq, e)

    return len(pq)


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: (x[0], x[1]))
print(solution())
