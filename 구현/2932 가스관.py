import sys
from collections import defaultdict

input = sys.stdin.readline

'''
상 우 하 좌 : 0 1 2 3
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
1 : 상0->우1, 좌3->하2
2 : 하2->우1, 좌3->상0
3 : 우1->상0, 하2->좌3
4 : 우1->하2, 상0->좌3
'''


def init():
    around['|'] = [0, 2]
    around['-'] = [1, 3]
    around['+'] = [0, 1, 2, 3]
    around['1'] = [1, 2]
    around['2'] = [0, 1]
    around['3'] = [0, 3]
    around['4'] = [2, 3]

    block[(0, 2)] = '|'
    block[(1, 3)] = '-'
    block[(0, 1, 2, 3)] = '+'
    block[(1, 2)] = '1'
    block[(0, 1)] = '2'
    block[(0, 3)] = '3'
    block[(2, 3)] = '4'

    return


def solution():
    global pos, answer

    init()
    for r in range(R):
        for c in range(C):
            if board[r][c] in ['Z', 'M', '.']:
                continue
            for d in around[board[r][c]]:
                nr = r + dr[d]
                nc = c + dc[d]

                if board[nr][nc] == '.':
                    answer.append((d + 2) % 4)
                    pos = [nr + 1, nc + 1]

    print(*pos, end=' ')
    print(block[tuple(sorted(answer))])
    return


R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
around = defaultdict(list)
block = defaultdict(str)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
pos = []
answer = []
solution()
