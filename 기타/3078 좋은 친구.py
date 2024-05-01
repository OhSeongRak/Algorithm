import sys

from collections import deque

input = sys.stdin.readline


def solution():
    count = 0

    name_sizes = [[] for _ in range(21)]
    for i in range(N):
        name_sizes[len(lst[i])].append(i)

    for ranks in name_sizes:
        if not ranks:
            continue

        queue = deque()
        for rank in ranks:
            while queue and rank - queue[0] > K:
                queue.popleft()

            count += len(queue)
            queue.append(rank)

    return count


N, K = map(int, input().split())
lst = [input().strip() for _ in range(N)]
print(solution())
