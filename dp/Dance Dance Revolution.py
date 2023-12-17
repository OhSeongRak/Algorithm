import sys

input = sys.stdin.readline


def get_power(next, x):
    if x == 0:
        return 2
    elif abs(next - x) == 2:
        return 4
    else:
        return 3


def solution():
    MAX_VALUE = sys.maxsize
    board = [[[MAX_VALUE for _ in range(5)] for _ in range(5)] for _ in range(N)]
    board[0][lst[0]][0] = 2
    board[0][0][lst[0]] = 2

    for i in range(1, N):
        next = lst[i]
        for l in range(5):
            for r in range(5):
                if board[i - 1][l][r] == MAX_VALUE:
                    continue

                if next == r or next == l:
                    board[i][l][r] = min(board[i][l][r], board[i - 1][l][r] + 1)
                    continue

                board[i][next][r] = min(board[i][next][r], board[i - 1][l][r] + get_power(next, l))
                board[i][l][next] = min(board[i][l][next], board[i - 1][l][r] + get_power(next, r))

    answer = MAX_VALUE
    for i in range(5):
        for j in range(5):
            answer = min(board[-1][i][j], answer)

    return answer


lst = list(map(int, input().split()))
N = len(lst) - 1
print(solution())

'''
0 -> ?: 2, 인접: 3, 반대: 4, 동일: 1
    1
2   0   4
    3

다음 위치에 두 발 중 하나가 있다면 1++,
현재 발 위치가 0이 아닐 경우,
abs(x - y) == 2 : 4
abs(x - y) == 0 : 1
else : 3

min(이 전 위치가 왼발일 때 오기, 오른발 일 때 오기)
'''
