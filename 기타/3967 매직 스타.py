import sys

input = sys.stdin.readline


def check():
    if ord(board[1][1]) + ord(board[1][3]) + ord(board[1][5]) + ord(board[1][7]) - ord('A') * 4 != 22:
        return False
    if ord(board[3][1]) + ord(board[3][3]) + ord(board[3][5]) + ord(board[3][7]) - ord('A') * 4 != 22:
        return False
    if ord(board[0][4]) + ord(board[1][3]) + ord(board[2][2]) + ord(board[3][1]) - ord('A') * 4 != 22:
        return False
    if ord(board[0][4]) + ord(board[1][5]) + ord(board[2][6]) + ord(board[3][7]) - ord('A') * 4 != 22:
        return False
    if ord(board[4][4]) + ord(board[3][3]) + ord(board[2][2]) + ord(board[1][1]) - ord('A') * 4 != 22:
        return False
    if ord(board[4][4]) + ord(board[3][5]) + ord(board[2][6]) + ord(board[1][7]) - ord('A') * 4 != 22:
        return False

    return True


def recur(index):
    if index == N:
        if check():
            for i in range(5):
                for j in range(9):
                    print(board[i][j], end='')
                print()
            exit()
        return

    r, c = lst[index]
    for i in range(12):
        if visited[i]:
            continue
        visited[i] = True
        board[r][c] = chr(i + 65)
        recur(index + 1)
        visited[i] = False
        board[r][c] = 'x'

    return


board = [list(input().strip()) for _ in range(5)]
lst = []
visited = [False] * 12
for r in range(5):
    for c in range(9):
        if board[r][c] == 'x':
            lst.append((r, c))
        elif board[r][c] != '.':
            visited[ord(board[r][c]) - ord('A')] = True

N = len(lst)
recur(0)
