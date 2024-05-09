import sys

input = sys.stdin.readline


def recur(result, idx):
    if idx == 26:
        return 1 if result == 0 else 0
    if not used[idx]:
        return recur(result, idx + 1)
    ret = 0
    for i in range(10):
        if not visited[i]:
            if is_first[idx] and i == 0:
                continue
            visited[i] = True
            ret += recur(result + count[idx] * i, idx + 1)
            visited[i] = False
    return ret


while N := int(input()):
    is_first = [False] * 26
    used = [False] * 26
    count = [0] * 26
    visited = [False] * 10
    for _ in range(N):
        word = input().strip()
        if len(word) > 1:
            is_first[ord(word[0]) - ord('A')] = True
        value = 1
        if _ == N - 1:
            value = -1
        for idx in range(len(word) - 1, -1, -1):
            used[ord(word[idx]) - ord('A')] = True
            count[ord(word[idx]) - ord('A')] += value
            value *= 10
    print(recur(0, 0))
