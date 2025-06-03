import sys

input = sys.stdin.readline


def recur(a, b, c):
    if visited[a][b][c]:
        return

    visited[a][b][c] = True
    if a == 0:
        answer.add(c)

    if a != 0:
        give = min(B - b, a)  # a에서 b로 옮길 수 있는 최대 리터
        recur(a - give, b + give, c)  # a -> b
        give = min(C - c, a)
        recur(a - give, b, c + give)  # a -> c

    if b != 0:
        give = min(A - a, b)
        recur(a + give, b - give, c)  # b -> a
        give = min(C - c, b)
        recur(a, b - give, c + give)  # b -> c

    if c != 0:
        give = min(A - a, c)
        recur(a + give, b, c - give)  # c -> a
        give = min(B - b, c)
        recur(a, b + give, c - give)  # c -> b

    return


visited = [[[False] * 201 for _ in range(201)] for _ in range(201)]
A, B, C = map(int, input().split())
answer = set()
recur(0, 0, C)
print(*sorted(list(answer)))
