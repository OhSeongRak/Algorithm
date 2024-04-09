import sys

from collections import deque

input = sys.stdin.readline
'''
1. 루돌프의 움직임
 - 아래, 오른, 왼, 위 순으로 움직임, bfs로 찾음.
 - 8번 계산해서 가까운 방향으로 이동

2. 충돌 확인
 - 산타가 있으면 산타를 C만큼 밀어버리고, 점수를 주고, 기절시킴
 - 밀린 곳에 산타가 있으면 상호작용

3. 산타의 움직임
 - 각 산타별로 루돌프와 가까운 위치로 이동 (상우하좌 순)
 - 해당 위치에 루돌프 있으면 밀림
 - 밀린 곳에 산타가 있으면 상호작용

4. 산타의 상태에 따라 1점씩 부여

5. 게임이 끝났는지 체크
'''


def check_santa(r, c):
    for i in range(P):
        if r == santas[i][0] and c == santas[i][1]:
            return i
    return -1


def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def move_rudolf():
    queue = deque()
    queue.append((rudolf[0], rudolf[1]))
    visited = [[False] * N for _ in range(N)]
    s_number = -1

    while queue:
        r, c = queue.popleft()
        visited[r][c] = True

        s_number = check_santa(r, c)
        if s_number != -1:
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not in_range(nr, nc) or visited[nr][nc]:
                continue

            queue.append((nr, nc))
            visited[nr][nc] = True


    return


N, M, P, C, D = map(int, input().split())  # 게임판 크기, 게임 턴 수, 산타 수, 루돌프 힘, 산타 힘
rudolf = list(map(int, input().split()))
rudolf[0] -= 1
rudolf[1] -= 1

santas = []
for _ in range(P):
    _, r, c = map(int, input().split())
    santas.append([r - 1, c - 1])

score, status = [0] * P, [0] * P  # 양의 정수면 기절 카운트, -1이면 탈락
dr, dc = [1, 0, 0, -1], [0, 1, -1, 0]

# Solution
for _ in range(M):
    move_rudolf()
