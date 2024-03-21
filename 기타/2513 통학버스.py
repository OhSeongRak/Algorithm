import sys, math

input = sys.stdin.readline


def solution():
    answer = 0
    avail = 0

    for pos, num in lst:  # 학교 기준 왼쪽
        if pos > S:
            break

        if num <= avail:  # 남은 자리에 탈 수 있다면, 태움
            avail -= num
            continue

        num -= avail  # 일단 가용인원 태움
        avail = 0
        count = math.ceil(num / K)  # 버스가 왕복 해야할 횟수
        answer += (S - pos) * 2 * count
        avail += K * count - num

    avail = 0
    for pos, num in lst[::-1]:  # 학교 기준 오른쪽
        if pos < S:
            break

        if num <= avail:  # 남은 자리에 탈 수 있다면, 태움
            avail -= num
            continue

        num -= avail # 일단 가용인원 태움
        avail = 0
        count = math.ceil(num / K)  # 버스가 왕복 해야할 횟수
        answer += (pos - S) * 2 * count
        avail += K * count - num

    return answer


N, K, S = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))
lst.sort()
print(solution())
