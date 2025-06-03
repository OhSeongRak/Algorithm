import sys

input = sys.stdin.readline


def solution():
    global lst
    answer = 0
    lst = lst + lst

    for i in range(N):
        tmp = set(lst[i:i + k])
        if c not in tmp:
            tmp.add(c)
        answer = max(len(tmp), answer)

    return answer


N, d, k, c = map(int, input().split())
lst = [int(input()) for _ in range(N)]
print(solution())
