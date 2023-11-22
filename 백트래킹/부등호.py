import sys
input = sys.stdin.readline

def cant(eq, a, b):
    if eq == '<':
        if a > b:
            return True
        
    if eq == '>':
        if a < b:
            return True
    
    return False


def recur(cnt, number):
    global maxNum, minNum

    if cnt == k:
        maxNum = max(maxNum, number)
        minNum = min(minNum, number)
        return

    for i in range(10):
        if selected[i]:
            continue
        
        if cant(lst[cnt], number[-1], str(i)):
            continue

        selected[i] = True
        recur(cnt + 1, number + str(i))
        selected[i] = False

    return

def solution():
    
    for i in range(10):
        selected[i] = True
        recur(0, str(i))
        selected[i] = False
    return

selected = [False] * 10
maxNum = '0' * 10
minNum = '9' * 10
k = int(input())
lst = list(input().split())
solution()
print(maxNum)
print(minNum)

