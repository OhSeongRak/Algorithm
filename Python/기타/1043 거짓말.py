import sys

input = sys.stdin.readline


def solution():
    global truth
    answer = 0

    for i in range(M):
        for party in party_list:
            for num in party:
                if num in truth:  # 진실을 아는 사람이 한명이라도 있으면
                    truth = truth.union(party)  # 해당 파티의 모든 사람에게 진실을 말해야함.
                    break

    for party in party_list:
        for num in party:
            if num in truth:
                break
        else:
            answer += 1

    return answer


N, M = map(int, input().split())
truth = set(input().split()[1:])
party_list = [set(input().split()[1:]) for _ in range(M)]
print(solution())
