import sys

input = sys.stdin.readline


def max_side(dice, b, t):  # 아래가 b이고 위가 t일 경우, 옆면의 최대값
    ret = 0
    for i in range(6):
        if i == b or i == t:
            continue
        ret = max(ret, dice[i])

    return ret


def solution():
    side = [5, 3, 4, 1, 2, 0]  # index의 반대편 index ex) 0->5, 1->3..

    answer = 0
    for b_index in range(6):
        hab = max_side(dices[0], b_index, side[b_index])  # 시작은 b_index를 아래로 했을 경우 옆면의 최대값
        top = dices[0][side[b_index]]  # 윗면 숫자
        top_index = side[b_index]  # 윗면 index

        for dice in dices[1:]:
            bottom_index = 0
            for i in range(6):
                if top == dice[i]:
                    bottom_index = i
                    top_index = side[i]
                    top = dice[side[i]]
                    break
            hab += max_side(dice, bottom_index, top_index)

        answer = max(answer, hab)

    return answer


N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
print(solution())
