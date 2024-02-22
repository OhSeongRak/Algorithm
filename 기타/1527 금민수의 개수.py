import sys
from collections import deque

input = sys.stdin.readline


def solution():
    numbers = []
    queue = deque([4, 7])

    while queue:
        n = queue.popleft()

        if n >= 1_000_000_000:
            continue

        numbers.append(n)
        queue.append(n * 10 + 4)
        queue.append(n * 10 + 7)

    answer = 0
    for n in numbers:
        if A <= n <= B:
            answer += 1

    return answer


A, B = map(int, input().split())
print(solution())
