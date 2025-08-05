import sys

input = sys.stdin.readline


def print_process(a, b):
    c = 6 - a - b
    print(a, c)
    print(a, b)
    print(c, b)


def move(N, a, b):
    global answer

    if N == 1:
        answer.append((a, b))
        return

    c = 6 - a - b
    move(N - 1, a, c)
    answer.append((a, b))
    move(N - 1, c, b)

    return


if __name__ == "__main__":
    N = int(input())
    answer = []
    move(N, 1, 3)
    print(len(answer))
    for a, b in answer:
        print(a, b)
