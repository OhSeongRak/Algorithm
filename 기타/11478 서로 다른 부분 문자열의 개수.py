import sys

input = sys.stdin.readline


def solution():
    answer = set()
    N = len(lst)
    for i in range(N):
        for j in range(i + 1, N):
            answer.add(lst[i:j])

    return len(answer)


lst = input()
print(solution())
