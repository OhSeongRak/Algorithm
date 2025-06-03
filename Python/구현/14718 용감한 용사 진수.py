import sys

input = sys.stdin.readline


def solution():
    answer = sys.maxsize

    for s1, _, _ in lst:
        for _, d1, _ in lst:
            for _, _, i1 in lst:
                cnt = 0
                for s2, d2, i2 in lst:
                    if s2 <= s1 and d2 <= d1 and i2 <= i1:
                        cnt += 1

                if cnt >= K:
                    answer = min(answer, s1 + d1 + i1)

    return answer


N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
print(solution())
