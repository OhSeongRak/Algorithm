import sys
from itertools import permutations

input = sys.stdin.readline


def solution():
    minVal, maxVal = MAX, -1 * MAX

    for operList in permutations(oper, N - 1):
        total = lst[0]

        for i in range(N - 1):
            if operList[i] == 0:
                total += lst[i + 1]
            elif operList[i] == 1:
                total -= lst[i + 1]
            elif operList[i] == 2:
                total *= lst[i + 1]
            elif operList[i] == 3:
                if total < 0:
                    total = -(-total // lst[i + 1])
                else:
                    total //= lst[i + 1]

            if total > MAX or total < -MAX:
                break

        maxVal = max(total, maxVal)
        minVal = min(total, minVal)

    print(maxVal)
    print(minVal)
    return


if __name__ == "__main__":
    N = int(input())
    MAX = 1000000000
    lst = list(map(int, input().split()))
    tmp = list(map(int, input().split()))
    oper = []
    for i in range(4):
        for j in range(tmp[i]):
            oper.append(i)
    solution()
