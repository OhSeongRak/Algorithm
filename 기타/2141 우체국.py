import sys

input = sys.stdin.readline


def solution():
    left, right = [0, pos_num[0][1]], [0, 0]
    for d, n in pos_num[1:]:
        right[0] += (d - pos_num[0][0]) * n
        right[1] += n

    answer = [right[0], pos_num[0][0]]

    for i in range(1, N):
        move = pos_num[i][0] - pos_num[i - 1][0]
        left[0] += move * left[1]
        left[1] += pos_num[i][1]
        right[0] -= move * right[1]
        right[1] -= pos_num[i][1]

        if left[0] + right[0] < answer[0]:
            answer = [left[0] + right[0], pos_num[i][0]]

    return answer[1]


N = int(input())
pos_num = [list(map(int, input().split())) for _ in range(N)]
pos_num.sort(key=lambda x: x[0])
print(solution())
