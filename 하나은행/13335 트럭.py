import sys
from collections import deque
input = sys.stdin.readline


def solution():
    time = 1
    queue = deque()
    bridge = L # 태울 수 있는 무게
    index = 0

    while True:
        # 트럭이 다 지나갔으면 빼자
        if queue and time - queue[0][1] == W:
            bridge += queue.popleft()[0]

        # 다리에 올릴 트럭이 있다면 올리자
        if index < N and bridge >= trucks[index]:
            queue.append((trucks[index], time))
            bridge -= trucks[index]
            index += 1

        if not queue and index == N:
            break
        time += 1

    return time


N, W, L = map(int, input().split()) # N개 트럭, 다리의 길이 W, 최대 하중 L
trucks = list(map(int, input().split()))
print(solution())
