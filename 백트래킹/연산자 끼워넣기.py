import sys
input = sys.stdin.readline


def recur(cur, op):
    global minAns, maxAns

    if cur == N-1:
        tmp = numbers[0]
        for i in range(N-1):
            if op[i] == 0:
                tmp += numbers[i+1]
            elif op[i] == 1:
                tmp -= numbers[i+1] 
            elif op[i] == 2:
                tmp *= numbers[i+1] 
            elif op[i] == 3:
                if tmp < 0:
                    tmp = abs(tmp) // numbers[i+1] * -1
                else:
                    tmp //= numbers[i+1] 

        maxAns = max(maxAns, tmp)
        minAns = min(minAns, tmp)
        return
    
    for i in range(N-1):
        if selected[i]:
            continue

        selected[i] = True
        recur(cur + 1, op + [lst[i]])
        selected[i] = False

    return

maxAns = -10000000000
minAns = 1000000000
N = int(input())
numbers = list(map(int, input().split()))
oper = list(map(int, input().split()))
lst = []
for i in range(4):
    tmp = [i] * oper[i]
    lst += tmp
selected = [False] * (N-1)
recur(0, [])
print(maxAns)
print(minAns)