import sys

input = sys.stdin.readline


def inclination(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def solution():
    answer = [0] * N

    for i in range(N):
        for j in range(i + 1, N):
            inc = inclination(i, lst[i], j, lst[j])
            for k in range(i + 1, j):
                tmp = inclination(i, lst[i], k, lst[k])
                if inc <= tmp:
                    break
            else:
                answer[i] += 1
                answer[j] += 1

    return max(answer)


N = int(input())
lst = list(map(int, input().split()))
print(solution())
