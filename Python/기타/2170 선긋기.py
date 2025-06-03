import sys

input = sys.stdin.readline


def solution():
    answer, start, end = 0, lst[0][0], lst[0][1]
    for i in range(N - 1):
        if end < lst[i + 1][0]:
            answer += end - start
            start = lst[i + 1][0]

        end = max(end, lst[i + 1][1])

    answer += end - start
    return answer


N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst.sort()
print(solution())
