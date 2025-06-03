import sys

input = sys.stdin.readline


def recur(T):
    global answer

    if len(T) == len(S):
        if T == S:
            answer = 1
        return

    if T[0] == 'B' and T[-1] == 'B':
        recur(T[1:][::-1])
    elif T[0] == 'A' and T[-1] == 'A':
        recur(T[:-1])
    elif T[0] == 'B' and T[-1] == 'A':
        recur(T[:-1])
        recur(T[1:][::-1])
    elif T[0] == 'A' and T[-1] == 'B':
        return

    return


S = input().strip()
T = input().strip()
answer = 0
recur(T)
print(answer)
