import sys

input = sys.stdin.readline


def can_move(r, c):
    if 0 <= r < N and 0 <= c < N and board[r][c] == 0 and not visited[r][c]:
        return True
    return False


def dfs(r, c, index):
    global answer

    if r == pos[index][0] and c == pos[index][1]:
        index += 1

    if index == M:
        answer += 1
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if not can_move(nr, nc):
            continue

        visited[nr][nc] = True
        dfs(nr, nc, index)
        visited[nr][nc] = False

    return


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
pos = []
for _ in range(M):
    r, c = map(int, input().split())
    pos.append((r - 1, c - 1))
visited = [[False for _ in range(N)] for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

answer = 0
visited[pos[0][0]][pos[0][1]] = True
dfs(pos[0][0], pos[0][1], 0)

print(answer)
# print(N, M)
# print(*board, sep='\n')
# print(*pos, sep='\n')

'''
3 3
0 0 0
0 0 0
0 0 1
3 1
1 2
2 3
'''
