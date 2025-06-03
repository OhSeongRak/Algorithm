import sys

input = sys.stdin.readline


def solution():
    ans1, ans2 = 10001, 0
    alpha = [[] for _ in range(26)]

    for i in range(len(st)):
        alpha[ord(st[i]) - ord('a')].append(i)

    for a in range(26):
        if len(alpha[a]) < K:
            continue

        for i in range(len(alpha[a]) - K + 1):
            ans1 = min(ans1, alpha[a][i + K - 1] - alpha[a][i] + 1)
            ans2 = max(ans2, alpha[a][i + K - 1] - alpha[a][i] + 1)

    if ans1 == 10001 or ans2 == 0:
        print(-1)
    else:
        print(ans1, ans2)

    return


T = int(input())
for _ in range(T):
    st = input().strip()
    K = int(input())
    solution()
