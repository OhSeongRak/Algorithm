import sys
input = sys.stdin.readline


def recur(cnt, index, numbers):
    if cnt == M:
        print(*numbers)
        return
    
    if index == N:
        return
    
    # 고르거나, 안고르거나
    recur(cnt + 1, index + 1, numbers + [lst[index]])
    recur(cnt, index + 1, numbers)

    return

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
recur(0, 0, [])