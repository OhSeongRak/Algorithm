import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def in_range(r, c):
    if 0 <= r < R and 0 <= c < C and not visited[r][c]:
        return True
    return False


def dfs(index, size):
    global answer
    r, c = index // C, index % C

    if r == R: # 마지막까지 다 체크를 했다면
        answer = max(answer, size)
        return

    if visited[r][c]: # 이미 현재 위치를 방문했다면
        dfs(index + 1, size)
        return

    for i in range(4): # r, c 기준으로 부메랑 만들기
        nr1 = r + dr[i]
        nc1 = c + dc[i]
        nr2 = r + dr[(i + 1) % 4]
        nc2 = c + dc[(i + 1) % 4]

        if not in_range(nr1, nc1) or not in_range(nr2, nc2):
            continue

        visited[r][c], visited[nr1][nc1], visited[nr2][nc2] = True, True, True
        dfs(index + 1, size + lst[r][c] * 2 + lst[nr1][nc1] + lst[nr2][nc2])
        visited[r][c], visited[nr1][nc1], visited[nr2][nc2] = False, False, False

    dfs(index + 1, size) # r, c를 포함시키지 않고 다음으로 넘어감
    return


R, C = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
answer = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
dfs(0, 0)
print(answer)
