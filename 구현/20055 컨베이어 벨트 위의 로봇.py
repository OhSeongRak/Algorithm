import sys

input = sys.stdin.readline


def solution():
    robot = [False] * N
    belt = [i for i in range(N)]
    answer = 0

    while lst.count(0) < K:

        for i in range(N):  # 벨트 이동
            belt[i] = (belt[i] - 1 + 2 * N) % (2 * N)

        for i in range(1, N)[::-1]:
            robot[i] = robot[i - 1]
        robot[0] = False
        robot[-1] = False

        for i in range(1, N)[::-1]:  # i-1 -> i로 로봇 옮김
            if lst[belt[i]] > 0 and not robot[i] and robot[i - 1]:
                robot[i] = robot[i - 1]
                robot[i - 1] = False
                lst[belt[i]] -= 1

        robot[-1] = False
        if not robot[0] and lst[belt[0]] > 0:
            robot[0] = True
            lst[belt[0]] -= 1

        answer += 1

    return answer


N, K = map(int, input().split())
lst = list(map(int, input().split()))
print(solution())
