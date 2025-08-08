import sys

input = sys.stdin.readline


def solution():
    dp = [lst[i] for i in range(N)]

    for cur in range(1, N):
        for prev in range(cur):
            if lst[prev] < lst[cur]:
                dp[cur] = max(dp[cur], lst[cur] + dp[prev])

    return max(dp)


if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    print(solution())

"""
import sys

input = sys.stdin.readline


def recur(cur, number):
    if cur == N:
        return 0

    total = 0
    if number < lst[cur]:
        total = recur(cur + 1, lst[cur]) + lst[cur]

    return max(total, recur(cur + 1, number))


if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))

    answer = 0
    print(recur(0, 0))
"""
