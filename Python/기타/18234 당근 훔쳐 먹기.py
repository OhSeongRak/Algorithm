import sys

from collections import deque

input = sys.stdin.readline


def solution():
    carrot.sort(key=lambda x: x[1])
    answer, day = 0, T - N

    for w, p in carrot:
        answer += w + p * day
        day += 1

    return answer


N, T = map(int, input().split())
carrot = []
for _ in range(N):
    carrot.append(list(map(int, input().split())))

print(solution())
