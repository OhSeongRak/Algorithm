import sys

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


def rudolf_to_santa(r1, c1, r2, c2):
    r, c = 0, 0
    if r2 - r1 != 0:
        r = (r2 - r1) // abs(r2 - r1)
    if c2 - c1 != 0:
        c = (c2 - c1) // abs(c2 - c1)

    return r, c


def santa_to_rudolf(r1, c1, r2, c2):
    distance = (r1 - r2) * (r1 - r2) + (c1 - c2) * (c1 - c2)
    drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ret_r, ret_c = 0, 0

    for dr, dc in drc:
        nr = r1 + dr
        nc = c1 + dc
        if not in_range(nr, nc) or check_santa(nr, nc) != -1:
            continue

        tmp = (nr - r2) * (nr - r2) + (nc - c2) * (nc - c2)
        if distance > tmp:
            ret_r, ret_c = dr, dc
            distance = tmp

    return ret_r, ret_c


def move_rudolf():
    s_info = [0, 0, 0, sys.maxsize]  # 산타 번호, r, c, 거리
    for i in range(P):
        if status[i] == -1:
            continue

        tmp = (rudolf[0] - santas[i][0]) * (rudolf[0] - santas[i][0]) + (rudolf[1] - santas[i][1]) * (
                rudolf[1] - santas[i][1])

        if tmp < s_info[3]:
            s_info = [i, santas[i][0], santas[i][1], tmp]
        elif tmp == s_info[3]:
            if s_info[1] < santas[i][0]:
                s_info = [i, santas[i][0], santas[i][1], tmp]
            elif s_info[1] == santas[i][0] and s_info[2] < santas[i][1]:
                s_info = [i, santas[i][0], santas[i][1], tmp]

    cr, cc = rudolf_to_santa(rudolf[0], rudolf[1], santas[s_info[0]][0], santas[s_info[0]][1])
    rudolf[0] += cr
    rudolf[1] += cc

    check_collision(cr, cc, C)
    return


def move_santa(number):
    sr, sc = santa_to_rudolf(santas[number][0], santas[number][1], rudolf[0], rudolf[1])
    santas[number][0] += sr
    santas[number][1] += sc

    if santas[number][0] == rudolf[0] and santas[number][1] == rudolf[1]:
        push_santa(number, -sr, -sc, D)
        score[i] += D
        if status[i] != -1:  # 퇴장되지 않았다면 기절
            status[i] = 2

    return


def push_santa(number, cr, cc, power):
    if not in_range(santas[number][0] + cr * power, santas[number][1] + cc * power):
        santas[number][0] += cr * power
        santas[number][1] += cc * power
        status[number] = -1
        return

    s = check_santa(santas[number][0] + cr * power, santas[number][1] + cc * power)
    if s != -1:
        push_santa(s, cr, cc, 1)

    santas[number][0] += cr * power
    santas[number][1] += cc * power

    return


def check_collision(cr, cc, power):
    for i in range(P):
        if rudolf[0] == santas[i][0] and rudolf[1] == santas[i][1]:
            push_santa(i, cr, cc, power)
            score[i] += power
            if status[i] != -1:  # 퇴장되지 않았다면 기절
                status[i] = 2
            break

    return


N, M, P, C, D = map(int, input().split())  # 게임판 크기, 게임 턴 수, 산타 수, 루돌프 힘, 산타 힘
rudolf = list(map(int, input().split()))
rudolf[0] -= 1
rudolf[1] -= 1

santas = [[0] * 2 for _ in range(P)]

for _ in range(P):
    n, r, c = map(int, input().split())
    santas[n - 1][0], santas[n - 1][1] = r - 1, c - 1

score, status = [0] * P, [0] * P  # 양의 정수면 기절 카운트, -1이면 탈락
dr, dc = [1, 0, 0, -1], [0, 1, -1, 0]

# Solution
for _ in range(M):
    move_rudolf()  # 루돌프 이동
    for i in range(P):
        if status[i] == 0:
            move_santa(i)  # 산타 이동

    for i in range(P):
        if status[i] != -1:  # 퇴장 아니면
            score[i] += 1
            status[i] = max(0, status[i] - 1)  # 기절 시간 줄임

    for i in range(P):
        if status[i] != -1:
            break
    else:
        break

print(*score)
