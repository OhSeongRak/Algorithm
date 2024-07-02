import math
import sys

input = sys.stdin.readline


def solution():
    N = len(lst)
    answer = [0] * N
    lst.sort()

    i, j = 0, 0
    while i < N:
        if i == N - 1 or lst[i] != lst[i + 1]:
            mid = math.floor(N / 2)
            if answer[mid] != 0:
                print("I'm Sorry Hansoo")
                return

            answer[mid] = lst[i]
            i += 1

        else:
            answer[j], answer[N - j - 1] = lst[i], lst[i]
            j += 1
            i += 2

    for k in answer:
        print(k, end='')
    return


lst = list(input().strip())
solution()
