import sys

input = sys.stdin.readline


def solution():
    answer = 0

    for i in range(N):
        expt = lst[:i] + lst[i + 1:]
        target = lst[i]
        l, r = 0, N - 2

        while l < r:
            if expt[l] + expt[r] == target:
                answer += 1
                break
            elif expt[l] + expt[r] < target:
                l += 1
            else:
                r -= 1

    return answer


N = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(solution())
