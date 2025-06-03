import sys

from collections import deque

input = sys.stdin.readline


def solution():
    ans = []
    queue = deque()

    for i in range(len(lst)):
        queue.append((lst[i], i + 1))

    while True:
        n, idx = queue.popleft()
        ans.append(idx)

        if not queue:
            break

        if n > 0:
            for i in range(n - 1):
                queue.append(queue.popleft())
        else:
            for i in range(-n):
                queue.appendleft(queue.pop())

    return ans


N = int(input())
lst = list(map(int, input().split()))
ans = solution()
for k in ans:
    print(k, end=' ')
