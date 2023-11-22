'''
36C3 x 선생님 위치마다 파악 => 충분
'''
import sys
from itertools import combinations

input = sys.stdin.readline


def find_teacher():
    lst = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'T':
                lst.append((r, c))
    return lst


def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def check():
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    tmp = [arr[:] for arr in board]
    for r, c in visited:
        tmp[r][c] = 'O'

    # print(*tmp, sep='\n')
    # print("==================================")

    for r, c in teachers:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            while in_range(nr, nc):
                if tmp[nr][nc] == 'O':
                    break
                elif tmp[nr][nc] == 'S':
                    return False

                nr += dr[i]
                nc += dc[i]

    return True


def comb(index, count):
    global answer

    if count == 3:
        if check():
            answer = 'YES'
        return

    for pos in range(index, N * N):
        r, c = pos // N, pos % N
        if (r, c) in visited or board[r][c] != 'X':
            continue
        visited.add((r, c))
        comb(pos + 1, count + 1)
        visited.remove((r, c))

    return


answer = 'NO'
N = int(input())
board = [list(input().split()) for _ in range(N)]
numbers = [k for k in range(N * N)]
visited = set()
teachers = find_teacher()
comb(0, 0)
print(answer)
