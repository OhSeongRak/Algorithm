import sys

input = sys.stdin.readline


def solution():
    global T

    while len(S) < len(T):
        if T.pop() == 'B':
            T.reverse()

    return int(S == T)


S = list(input().strip())
T = list(input().strip())
print(solution())
