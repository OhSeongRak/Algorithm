import sys

input = sys.stdin.readline


def solution():
    # dp[i][j] = i번 도시에 j개의 도시를 거쳐서 도달했을 때의 최대 기내식 점수
    dp = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]
    dp[1][1] = 0  # 1번 도시에서 시작 (1개 도시 방문, 점수 0)

    for j in range(1, M):  # j개 도시를 방문한 상태에서
        for i in range(1, N):  # i번 도시에서
            if dp[i][j] == -1:  # 도달할 수 없는 상태면 스킵
                continue

            # i번 도시에서 k번 도시로 이동 (j+1개 도시 방문)
            for k in range(i + 1, N + 1):  # 더 큰 번호의 도시로만 이동
                if board[i][k] > 0:  # 직항이 있으면
                    dp[k][j + 1] = max(dp[k][j + 1], dp[i][j] + board[i][k])

    # N번 도시에 도달한 경우 중 최댓값
    answer = 0
    for j in range(1, M + 1):
        if dp[N][j] != -1:
            answer = max(answer, dp[N][j])

    return answer


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    board = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for _ in range(K):
        start, end, value = map(int, input().split())
        if start < end:  # 더 큰 번호로만 이동 가능
            board[start][end] = max(value, board[start][end])

    print(solution())