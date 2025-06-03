import sys

from collections import deque

input = sys.stdin.readline


def solution():
    queue = deque([i + 1 for i in range(N)])
    count = 0

    for k in lst:
        idx = queue.index(k)
        if len(queue) - idx < idx:
            while queue[0] != k:
                queue.appendleft(queue.pop())
                count += 1
        else:
            while queue[0] != k:
                queue.append(queue.popleft())
                count += 1

        queue.popleft()

    return count


N, M = map(int, input().split())
lst = list(map(int, input().split()))
print(solution())
