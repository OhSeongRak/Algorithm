import sys

input = sys.stdin.readline

'''
완탐인 경우
- recur(반알 개수, 한알 개수):
'''


def recur(half, whole):
    global total

    if half == 0 and whole == 0:
        total += 1
        return

    if half > 0:
        recur(half - 1, whole)
    if whole > 0:
        recur(half + 1, whole - 1)
    return


N = int(input())
while N != 0:
    total = 0
    recur(0, N)
    print(total)
    N = int(input())

