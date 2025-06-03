import sys

from heapq import heappush, heappop, heapify

input = sys.stdin.readline


def solution():
    pq = []
    for k in lst:
        heappush(pq, k)

    answer = 0
    while len(pq) > 1:
        p1, p2 = heappop(pq), heappop(pq)
        answer += p1 + p2
        heappush(pq, p1 + p2)

    return answer


T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    print(solution())
