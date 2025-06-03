import sys

input = sys.stdin.readline


def copy(origin):
    board = [[0] * 7 for _ in range(7)]
    for i in range(7):
        for j in range(7):
            board[i][j] = origin[i][j]

    return board


def drop(col):
    board = copy(origin)

    for i in range(7)[::-1]:
        if board[i][col] == 0:
            board[i][col] = N
            break

    return board


def can_remove(board, i, j):
    garo, sero = 1, 1

    r = i - 1
    while board[r][j] != 0:  # 아래쪽으로
        sero += 1
        r -= 1

    r = i + 1
    while board[r][j] != 0:  # 위쪽으로
        sero += 1
        r += 1

    c = j - 1
    while board[i][c] != 0:  # 왼쪽으로
        garo += 1
        c -= 1

    c = j + 1
    while board[i][c] != 0:  # 오른쪽으로
        garo += 1
        c += 1

    return board[i][j] == garo or board[i][j] == sero


def check(tmp):
    # 연속된 값 계산하기 편하게 하기 위해 테투리 0으로 둘러싸기
    board = [[0] * 9 for _ in range(9)]
    for i in range(7):
        for j in range(7):
            board[i + 1][j + 1] = tmp[i][j]
    # print(*board, sep='\n')

    removed = []
    # 하나하나 따져가면서 없어지는 숫자의 위치 removed에 추가
    for i in range(1, 8):
        for j in range(1, 8):
            if board[i][j] == 0:
                continue

            if can_remove(board, i, j):
                removed.append((i - 1, j - 1))

    return removed


def down(board):
    ret = [[0] * 7 for _ in range(7)]

    for c in range(7):
        h = 6
        for r in range(7)[::-1]:
            if board[r][c] != 0:
                ret[h][c] = board[r][c]
                h -= 1

    return ret


def count_ball(board):
    count = 0
    for i in range(7):
        for j in range(7):
            if board[i][j] != 0:
                count += 1

    return count


def solution():
    answer = 49

    for c in range(7):
        board = drop(c)
        while True:
            removed = check(board)
            if not removed:
                break
            # board에서 지우고
            for R, C in removed:
                board[R][C] = 0
            board = down(board)  # 없어진 부분 내리기

        # 남아있는 공 개수 비교
        answer = min(count_ball(board), answer)

    return answer


origin = [list(map(int, input().split())) for _ in range(7)]
N = int(input())
print(solution())
