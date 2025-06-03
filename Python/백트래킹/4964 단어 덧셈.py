import sys

from itertools import permutations

input = sys.stdin.readline


def check(convert, perm):
    left, right = 0, 0
    # if perm[0] == 9:
    #     print(convert, perm)
    for i in range(N):
        word, total = lst[i], 0
        for k in word:
            num = perm[convert.index(k)]
            if num == 0 and total == 0 and len(word) > 1:
                return False
            total = total * 10 + num

        if i == N - 1:
            right += total
        else:
            left += total

    return left == right


def solution():
    convert = []

    for word in lst:
        for k in word:
            if k not in convert:
                convert.append(k)

    count = 0
    for perm in permutations(range(10), len(convert)):
        if check(convert, perm):
            count += 1

    return count


while True:
    N = int(input())
    if N == 0:
        break
    lst = [input().strip() for _ in range(N)]
    print(solution())
