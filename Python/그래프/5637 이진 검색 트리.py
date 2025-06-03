import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def recur(start, end):
    if start == end:
        return

    mid = end
    for i in range(start + 1, end):
        if pre[start] < pre[i]:
            mid = i
            break

    recur(start + 1, mid)
    recur(mid, end)
    print(pre[start])

    return


pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

N = len(pre)
recur(0, N)
