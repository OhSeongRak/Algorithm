import heapq
import sys

from collections import deque
from heapq import heappop, heapify

input = sys.stdin.readline


def solution():
    queue, pq, count = deque(), [], 1

    for i in range(N):
        queue.append((lst[i], i))
        pq.append(-lst[i])
    heapify(pq)

    while True:
        important, number = queue.popleft()
        if -pq[0] == important:
            if number == M:
                return count
            count += 1
            heappop(pq)

        else:
            queue.append((important, number))


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    print(solution())
