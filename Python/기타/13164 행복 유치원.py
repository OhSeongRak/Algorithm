import sys

input = sys.stdin.readline

'''
팀을 나눈다 -> 나눈 부분에서의 차이만큼 준다.
ex)
1 3 5 6 10

팀이 1개인 경우,
10 - 1 => 9

팀이 2개인 경우,
1 / 3 5 6 10 : 1과 3의 차이만큼 줄어듦
1 3 / 5 6 10 : 3과 5의 차이만큼 줄어듦

팀이 3개인 경우,
1 / 3 / 5 6 10 : 1과 3의 차이, 3과 5의 차이만큼 줄어듦
1 3 / 5 6 / 10 : 3과 5의 차이, 6과 10의 차이만큼 줄어듦

즉, 각 숫자 별 차이의 최대값을 차례대로 빼면 됨.
'''


def solution():
    diff = []  # 오른쪽 친구와의 차이
    for i in range(N - 1):
        diff.append(lst[i + 1] - lst[i])
    diff.sort(reverse=True)

    answer = lst[-1] - lst[0]  # 팀이 1개인 경우
    for i in range(K - 1):  # 차이가 큰 값부터 빼줌
        answer -= diff[i]

    return answer


N, K = map(int, input().split())
lst = list(map(int, input().split()))
print(solution())
