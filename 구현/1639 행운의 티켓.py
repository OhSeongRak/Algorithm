import sys

input = sys.stdin.readline


def solution():
    N = len(S)
    answer = 0

    for i in range(N - 1):
        cnt = 1
        while i + cnt * 2 <= N:
            if sum(S[i:i + cnt]) == sum(S[i + cnt:i + cnt * 2]):
                answer = max(answer, cnt * 2)
            cnt += 1

    return answer


S = list(map(int, input().strip()))
print(solution())
