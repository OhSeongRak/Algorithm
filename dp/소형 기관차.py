import sys

input = sys.stdin.readline


def solution():
    global lst

    lst = [0] + lst
    # 누적합 구하기
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + lst[i]

    '''
    r: 소형 기관차 개수
    c: c번째에서의 최대값
    dp[r][c] : r개의 소형차가 c번째 위치에서 태울 수 있는 최대 손님 수
    '''
    dp = [[0 for i in range(N + 1)] for _ in range(4)]

    for r in range(1, 4):
        # r * K : 이 위치가 r개의 소형차가 K개의 객차를 고를 수 있는 최소 위치
        for c in range(r * K, N + 1):
            # r개의 객차가 c를 고른다 => 누적합[c] - 누적합[c-K] + r-1개의 객차가 c-K에서 고른 최대 손님 수
            # r개의 객차가 c를 고르지 않는다 => r개의 객차가 c-1까지에서 고른 최대 손님 수
            dp[r][c] = max(dp[r - 1][c - K] + prefix_sum[c] - prefix_sum[c - K], dp[r][c - 1])

    return dp[3][-1]


N = int(input())
lst = list(map(int, input().split()))
K = int(input())
print(solution())

'''    35   40  50   10   30   45   60
0   35   75  125  135  165  210  270
연속된 K개의 객차을 3번 고를 때의 최대 값
'''
