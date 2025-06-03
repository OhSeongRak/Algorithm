N, M = 4, 9 # M을 만들어라
A = [1, 3]
B = [2, 4]

dp = [-1] * (M + 1)

for b in B:
    dp[b] = 1
    for i in range(1, M + 1)[::-1]: # 앞에서부터 하면 b가 여러번 사용됨
        if i != b and dp[i] != -1 and i + b <= M:
            if dp[i + b] == -1: # 처음일 경우
                dp[i + b] = dp[i] + 1
            else:
                dp[i + b] = min(dp[i + b], dp[i] + 1)

for a in A:
    dp[a] = 1
    for i in range(1, M + 1): # a는 여러번 사용해도 되니 앞에서부터
        if dp[i] != -1 and i + a <= M:
            if dp[i + a] == -1: # 처음일 경우
                dp[i + a] = dp[i] + 1
            else:
                dp[i + a] = min(dp[i + a], dp[i] + 1)

print(dp[M])