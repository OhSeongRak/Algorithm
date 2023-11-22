import sys
input = sys.stdin.readline


def recur(cur, start, numbers):
    if cur == M:
        print(*numbers)
        return
    
    for i in range(start, N):
        recur(cur + 1, i, numbers + [i+1])

    return

N, M = map(int, input().split())
recur(0, 0, [])