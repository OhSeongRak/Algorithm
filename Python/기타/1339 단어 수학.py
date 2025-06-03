import sys

input = sys.stdin.readline


def solution():
    alphas = [0] * 26
    for word in words:
        n = 0
        for alpha in word[::-1]:
            alphas[ord(alpha) - ord('A')] += 10 ** n
            n += 1

    alphas.sort(reverse=True)
    answer = 0
    for i in range(10):
        answer += alphas[i] * (9 - i)

    return answer


N = int(input())
words = [list(input().strip()) for _ in range(N)]
print(solution())
