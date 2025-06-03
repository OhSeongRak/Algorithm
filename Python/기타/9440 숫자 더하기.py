import sys

input = sys.stdin.readline


def solution():
    lst.sort()
    num = ["", ""]
    idx1, idx2 = 0, 0

    for i in range(len(lst)):
        if lst[i] == 0:
            continue
        num[0] += str(lst[i])
        num[1] += str(lst[i + 1])
        idx1, idx2 = i, i + 1
        break

    for i in range(len(lst)):
        if i == idx1 or i == idx2:
            continue
        num[i % 2] += str(lst[i])

    return int(num[0]) + int(num[1])


while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    lst = lst[1:]
    print(solution())
