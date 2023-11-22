import sys
from collections import defaultdict
input = sys.stdin.readline

def checkNumbers(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return False
    
    return True

def recur(index, numbers):
    global answer

    if index == N:
        if checkNumbers(numbers):
            return 0
        return -10000000000 

    return max(recur(index + 1, numbers + [lst[index]]) + 1,
               recur(index + 1, numbers))
    return

N = int(input())
lst = [0] * N
tmp = []
answer = 0
for _ in range(N):
    tmp.append(list(map(int, input().split())))

tmp.sort()
for i in range(N):
    lst[i] = tmp[i][1]
# print(lst)
print(N - recur(0, []))







# 최소한으로 자르자!
# 교차 조건
# A 입장에서 내 전 전깃줄들이 B보다 작아야함


