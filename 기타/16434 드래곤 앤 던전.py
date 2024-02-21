import sys, math

input = sys.stdin.readline


# 해당 몬스터랑 싸울 때 필요한 최소 hp
def fight(hero_a, mon_a, mon_h):
    count = math.ceil(mon_h / hero_a)
    return mon_a * (count - 1)


def solution():
    max_hp, cur_hp, need_hp, atk = 1, 1, 0, H_atk

    for t, a, h in room:
        if t == 1:
            need_hp += fight(atk, a, h)  # 몬스터를 만났을 때 필요한 hp
        else:
            if cur_hp <= need_hp:  # 현재 hp보다 필요 hp가 더 클때
                max_hp += (need_hp - cur_hp) + 1  # 0이 되면 사망하기 때문에
                cur_hp = 1
            else:
                cur_hp -= need_hp

            need_hp = 0
            cur_hp = min(max_hp, cur_hp + h)
            atk += a

    if cur_hp <= need_hp:
        max_hp += (need_hp - cur_hp) + 1

    return max_hp


N, H_atk = map(int, input().split())
room = []
for _ in range(N):
    room.append(list(map(int, input().split())))
print(solution())
