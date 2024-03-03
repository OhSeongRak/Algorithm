import sys

from itertools import permutations

input = sys.stdin.readline


def check(line):
    for cur in range(N):
        cnt = 0
        for i in range(cur):
            if line[cur] < line[i]:
                cnt += 1
        if cnt != left[line[cur]]:
            return False

    return True


def solution():
    for line in permutations(range(N)):
        if check(line):
            for num in line:
                print(num + 1, end=' ')
            return

    return


N = int(input())
left = list(map(int, input().split()))
solution()
