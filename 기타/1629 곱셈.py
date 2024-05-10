import sys

input = sys.stdin.readline


def recur(num, count):
    if count == 1:
        return num % C

    div = recur(num, count // 2)
    if count % 2 == 0:
        return (div * div) % C
    else:
        return (div * div * A) % C


A, B, C = map(int, input().split())
print(recur(A, B))
