import sys
from itertools import permutations

input = sys.stdin.readline


def is_valid(board):
    for i in range(9):  # 다 채워졌는지 확인
        if board[i // 3][i % 3] not in ['X', 'O']:
            break
    else:
        return True

    for r in range(3):  # 가로
        for c in range(1, 3):
            if board[r][c - 1] != board[r][c]:
                break
        else:
            return True

    for c in range(3):  # 세로
        for r in range(1, 3):
            if board[r - 1][c] != board[r][c]:
                break
        else:
            return True

    if board[0][0] == board[1][1] == board[2][2]:
        return True

    if board[2][0] == board[1][1] == board[0][2]:
        return True

    return False


def solution():
    xList, oList = [], []

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                xList.append((i, j))
            elif board[i][j] == 'O':
                oList.append((i, j))

    if len(xList) - len(oList) != 1 and len(xList) - len(oList) != 0:
        return "invalid"

    for X in permutations(xList, len(xList)):
        for O in permutations(oList, len(oList)):
            tmp = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            for i in range(len(X) + len(O)):
                if is_valid(tmp):
                    break

                if i % 2 == 0:
                    tmp[X[i // 2][0]][X[i // 2][1]] = 'X'
                else:
                    tmp[O[i // 2][0]][O[i // 2][1]] = 'O'

            else:
                if is_valid(tmp):
                    return "valid"

    return "invalid"


while True:
    lst = list(input().rstrip())
    if lst[0] == 'e':
        break

    board = []
    for i in range(3):
        board.append(lst[i * 3:i * 3 + 3])

    print(solution())
