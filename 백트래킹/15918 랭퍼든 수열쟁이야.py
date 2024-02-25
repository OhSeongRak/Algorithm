import sys

input = sys.stdin.readline


def recur(number):
    global answer

    if number == fixed_value:
        recur(number + 1)
        return

    if number > N:
        answer += 1
        return

    for i in range(1, 2 * N - number):
        if lst[i] == 0 and lst[i + number + 1] == 0:
            lst[i] = number
            lst[i + number + 1] = number
            recur(number + 1)
            lst[i] = 0
            lst[i + number + 1] = 0
    return


N, x, y = map(int, input().split())
lst = [0] * 25
answer = 0
fixed_value = y - x - 1
lst[x], lst[y] = fixed_value, fixed_value
recur(1)
print(answer)
