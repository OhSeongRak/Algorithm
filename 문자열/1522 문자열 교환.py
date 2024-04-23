import sys

from collections import deque

input = sys.stdin.readline


def solution():
    if 'b' not in lst:
        return 0

    tmp1, tmp2 = lst.copy(), lst.copy()
    while tmp1[-1] == 'a':
        tmp1.appendleft(tmp1.pop())

    while tmp2[0] == 'a':
        tmp2.append(tmp2.popleft())

    l, r = 0, len(lst) - 1
    count1, count2 = 0, 0

    while l < r:
        if tmp1[l] == 'b' and tmp1[r] == 'a':
            # lst[l], lst[r] = lst[r], lst[l]
            count1 += 1
            l += 1
            r -= 1
            continue

        if tmp1[l] == 'a':
            l += 1
        if tmp1[r] == 'b':
            r -= 1

    l, r = 0, len(lst) - 1
    while l < r:
        if tmp2[l] == 'a' and tmp2[r] == 'b':
            # lst[l], lst[r] = lst[r], lst[l]
            count2 += 1
            l += 1
            r -= 1
            continue

        if tmp2[l] == 'b':
            l += 1
        if tmp2[r] == 'a':
            r -= 1

    return min(count1, count2)


lst = deque(list(input().strip()))
print(solution())
