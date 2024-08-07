import sys

input = sys.stdin.readline


def solution():
    lst = [0] * (N + 2)
    answer = 0

    for i in range(N):
        if lst[i] != origin[i]:
            for j in range(i, i + 3):
                lst[j] = 1 - lst[j]
            answer += 1

    return answer


N = int(input())
origin = list(map(int, input().split()))
print(solution())
