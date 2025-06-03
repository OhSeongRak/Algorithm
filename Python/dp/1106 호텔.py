import sys

input = sys.stdin.readline


def solution():
    max_value = sys.maxsize
    dp = [max_value] * (C + 1) # i명을 데려올 때 드는 최소 비용
    dp[0] = 0

    for v, c in lst: # v원에 c명을 데려올 수 있음
        for j in range(C + 1):
            if j + c > C: # C명을 넘어서도 되기 때문에
                dp[C] = min(dp[C], dp[j] + v)
            else:
                # j+c명을 데려올 때 드는 최소 비용
                # => j명을 데려올 때 드는 최소 비용 + v원(을 써서 c명을 데려올 수 있기 때문에)
                dp[j + c] = min(dp[j + c], dp[j] + v)

    return dp[-1]


C, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
print(solution())
