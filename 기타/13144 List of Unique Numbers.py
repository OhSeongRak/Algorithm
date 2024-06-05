import sys

input = sys.stdin.readline


def solution():
    answer = 0
    visited = [False] * 100001
    l, r = 0, 0

    while r < N:
        if not visited[lst[r]]:
            visited[lst[r]] = True
            r += 1
            answer += r - l
        else:
            visited[lst[l]] = False
            l += 1

    return answer


N = int(input())
lst = list(map(int, input().split()))
print(solution())
