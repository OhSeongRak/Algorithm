import sys

from collections import deque

input = sys.stdin.readline


def solution():
    visited = [False] * N
    answer = 0
    queue = deque()

    for i in range(N)[::-1]:  # 뒤에서부터 A와 B를 지움
        if lst[i] == 'A':
            if queue:
                visited[queue.popleft()] = True
                answer += 1
        elif lst[i] == 'B':
            queue.append(i)

    queue = deque()
    for i in range(N)[::-1]:  # 뒤에서부터 남은 B와 C를 지움
        if visited[i]:
            continue
        if lst[i] == 'B':
            if queue:
                queue.popleft()
                answer += 1
        elif lst[i] == 'C':
            queue.append(i)

    return answer


lst = list(input().strip())
N = len(lst)
print(solution())
