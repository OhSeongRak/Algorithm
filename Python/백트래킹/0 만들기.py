import sys

input = sys.stdin.readline


def calculate(st):
    numbers, op, cur = [], [], 0
    for k in st:
        if k in ['+', '-']:
            op.append(k)
            numbers.append(cur)
            cur = 0
        elif k == " ":
            continue
        else:
            cur = cur * 10 + int(k)

    numbers.append(cur)
    answer = numbers[0]
    for i in range(len(op)):
        if op[i] == '+':
            answer += numbers[i + 1]
        else:
            answer -= numbers[i + 1]

    return True if answer == 0 else False


def print_list(arr):
    for i in range(N - 1):
        print(i + 1, end="")
        print(arr[i], end="")
    print(N)
    return


def recur(index, st):
    if index == N - 1:
        if calculate(st):
            print(st)
        return

    recur(index + 1, st + " " + str(index + 2))
    recur(index + 1, st + "+" + str(index + 2))
    recur(index + 1, st + "-" + str(index + 2))
    return


test_case = int(input())
for _ in range(test_case):
    N = int(input())
    recur(0, "1")
    print()