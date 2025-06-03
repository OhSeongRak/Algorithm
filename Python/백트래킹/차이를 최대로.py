import sys
input = sys.stdin.readline


def recur(cur, numbers):
    global answer

    if cur == N:
        tmp = 0
        for i in range(N-1):
            tmp += abs(numbers[i] - numbers[i+1])
        answer = max(answer, tmp)
        return
    
    for i in range(N):
        if selected[i]:
            continue

        selected[i] = True
        recur(cur + 1, numbers + [lst[i]])
        selected[i] = False

    return

answer = -100000
N = int(input())
selected = [False] * N
lst = list(map(int, input().split()))
recur(0, [])
print(answer)