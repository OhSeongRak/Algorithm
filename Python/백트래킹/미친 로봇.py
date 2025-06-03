import sys

input = sys.stdin.readline


def solution(N, lst):
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    for i in range(len(lst)):
        lst[i] /= 100
    answer = 0
    visited = [[False] * 15 for _ in range(15)]

    def recur(prob, index, r, c):
        nonlocal answer, visited

        if index == N:
            answer += prob
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if lst[i] == 0 or visited[nr][nc]:
                continue

            visited[nr][nc] = True
            recur(prob * lst[i], index + 1, nr, nc)
            visited[nr][nc] = False

        return

    visited[0][0] = True
    recur(1, 0, 0, 0)
    return answer


tmp = list(map(int, input().split()))
N = tmp[0]
lst = [k for k in tmp[1:]]
print(solution(N, lst))

'''
0, 0 부터 시작한다 치자
dr, dc로 방향 동서남북으로 맞추고 확률은 /100해서 맞춤
일단 완탐 ㄱ
'''
