import sys

input = sys.stdin.readline


def solution():
    answer = set()

    for start in range(1, N + 1):
        visited = [False] * (N + 1)
        tmp = set()
        cur = start
        while not visited[cur]:
            visited[cur] = True
            tmp.add(cur)
            cur = lst[cur]

        if cur == start:
            answer = answer.union(tmp)

    answer = sorted(list(answer))

    print(len(answer))
    for k in answer:
        print(k)
    return


N = int(input())
lst = [0]
for _ in range(N):
    lst.append(int(input()))
solution()
