import sys

input = sys.stdin.readline


def recur(index):
    global answer

    if index == N:
        tmp = 0
        for i in range(N):
            tmp += lst[selected[i]]
            tmp -= K
            if tmp < 0:
                return

        answer += 1
        return

    for i in range(N):
        if i in selected:
            continue
        selected[index] = i
        recur(index + 1)
        selected[index] = -1

    return


N, K = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0
selected = [-1] * N
recur(0)
print(answer)
