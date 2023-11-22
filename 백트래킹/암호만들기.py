import sys
input = sys.stdin.readline


def recur(cnt, index, moCnt, jaCnt, alphas):
    if cnt == N:
        if moCnt >= 1 and jaCnt >= 2:
            print(alphas)
        return
    
    if index == M:
        return
    
    # 고르거나, 안고르거나
    if lst[index] in vowels:
        recur(cnt + 1, index + 1, moCnt + 1, jaCnt, alphas + lst[index])
    else:
        recur(cnt + 1, index + 1, moCnt, jaCnt + 1, alphas + lst[index])

    recur(cnt, index + 1, moCnt, jaCnt, alphas)

    return

vowels = ['a','e','i','o','u']
N, M = map(int, input().split())
lst = sorted(input().split())
recur(0, 0, 0, 0, '')