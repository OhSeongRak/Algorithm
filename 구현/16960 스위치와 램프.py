import sys

input = sys.stdin.readline


def solution():
    for switch in switches:
        for l in switch:
            if lamp[l] == 1:
                break
        else:
            return 1

    return 0


N, M = map(int, input().split())
switches = []
lamp = [0] * (M + 1)

for i in range(N):
    switches.append(list(map(int, input().split()))[1:])
    for l in switches[i]:
        lamp[l] += 1

print(solution())
