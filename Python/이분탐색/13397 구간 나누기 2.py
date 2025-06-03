import sys

input = sys.stdin.readline


def check(mid):
    count = 1
    min_val = max_val = lst[0]

    for i in range(1, N):
        if abs(lst[i] - min_val) > mid or abs(lst[i] - max_val) > mid:
            count += 1
            min_val = max_val = lst[i]
        else:
            min_val = min(min_val, lst[i])
            max_val = max(max_val, lst[i])

    return count


def solution():
    l, r = 0, max(lst) - min(lst)
    answer = r

    while l <= r:
        mid = (l + r) // 2
        count = check(mid)

        if count <= M:
            answer = min(answer, mid)
            r = mid - 1
        else:
            l = mid + 1

    return answer


N, M = map(int, input().split())
lst = list(map(int, input().split()))
# print(check(98))
print(solution())
