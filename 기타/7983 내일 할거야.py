import sys

input = sys.stdin.readline


def solution():
    answer = lst[0][1]

    for d, t in lst:
        answer = min(answer, t)
        answer -= d

    return answer


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: x[1], reverse=True)
# print(*lst, sep='\n')
print(solution())
