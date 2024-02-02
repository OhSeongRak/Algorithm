import sys
from collections import deque

input = sys.stdin.readline


def solution():
    global lst
    answer = ""

    for _ in range(N):
        l, r, flag = 0, len(lst) - 1, ""
        while l <= r:
            if lst[l] == lst[r]:
                l += 1
                r -= 1

            else:
                if lst[l] < lst[r]:
                    flag = "left"
                else:
                    flag = "right"
                break

        if flag == "left":
            answer += lst.popleft()
        else:
            answer += lst.pop()

    i = 0
    while i <= N:
        print(answer[i:i + 80])
        i += 80

    return


N = int(input())
lst = deque()
for _ in range(N):
    lst.append(input().strip())
solution()
