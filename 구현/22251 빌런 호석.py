import sys

input = sys.stdin.readline


def change(lst):
    return int(''.join(map(str, lst)))


def diff(a, b):
    ret = 0
    for i in range(7):
        ret += 0 if number[a][i] == number[b][i] else 1

    return ret


def recur(lst, count, index):
    global answer

    if P < count:
        return

    if index == K:
        if N < change(lst) or change(lst) == 0:
            return
        # print(lst)
        answer += 1
        return

    for num in range(10):
        ori = lst[index]
        lst[index] = num
        recur(lst, count + diff(ori, num), index + 1)
        lst[index] = ori

    return


number = [[1, 1, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0, 1],
          [1, 0, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 1],
          [1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 0, 1, 1]]

N, K, P, X = map(int, input().split())
origin = [0] * K
back, tmp = -1, X

while tmp > 0:
    origin[back] = tmp % 10
    tmp = tmp // 10
    back -= 1

answer = 0
recur(origin, 0, 0)
print(answer - 1)
