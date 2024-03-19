import sys

input = sys.stdin.readline
'''
D의 거리에 (N-M)개의 돌을 놓을 경우, D // (N-M+1) 이 최소 거리의 최댓값이 된다.
answer = D // (N-M+1)부터 시작하여 이분 탐색.
'''


def solution():
    answer, l, r = 0, 0, D

    while l <= r:
        mid = (l + r) // 2

        count = 0  # 거리가 mid 이상 되기 위해 제거되는 돌의 개수
        start, end = 0, 1
        while end < len(lst):
            if lst[end] - lst[start] < mid:
                count += 1
                end += 1
            else:
                start = end
                end += 1

        if M < count:  # 최소거리의 최댓값이 mid가 될 수 없다면
            r = mid - 1
        else:
            answer = mid
            l = mid + 1

    return answer


D, N, M = map(int, input().split())
lst = [0, D]
for _ in range(N):
    lst.append(int(input()))
lst.sort()
print(solution())
