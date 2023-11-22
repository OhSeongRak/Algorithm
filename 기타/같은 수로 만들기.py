import sys
input = sys.stdin.readline


def solution():
    prev, ans = lst[0], 0
    for cur in lst[1:]:
        if prev < cur:  # 이전값보다 현재값이 크면 차이만큼 증가
            ans += cur - prev
        prev = cur  # 같거나, 작으면 따로 해줄게 없음

    return ans + max(lst) - prev  # 마지막으로 끝난 값(prev)과 최대로 도달해야하는 값의 차이만큼 추가


N = int(input())
lst = [int(input()) for _ in range(N)]
print(solution())
