import math
import sys

input = sys.stdin.readline


def solution():
    cur = 0
    answer = 0

    for start, end in lst:
        start = max(cur, start)
        count = math.ceil((end - start) / L)
        answer += count
        cur = start + L * count

    return answer


N, L = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: x[0])
print(solution())
