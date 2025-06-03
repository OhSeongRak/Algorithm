import sys
from collections import defaultdict

input = sys.stdin.readline


def solution(m):

    return dic[m] * (N - dic[m] - 1)


N, Q = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

dic = defaultdict(int)
for i in range(N):
    dic[lst[i]] = i

for _ in range(Q):
    print(solution(int(input())))

'''
3개를 골라서 평균 m이 나오게 하도록 해봐라.
일단 정렬?

5 3
5 2 3 1 6
1
3
6
'''
