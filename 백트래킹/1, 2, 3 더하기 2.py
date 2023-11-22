import sys
input = sys.stdin.readline

def recur(lst):
    hab = sum(lst)
    if hab > N:
        return
    
    if hab == N:
        tmp = str(lst[0])
        for i in range(1, len(lst)):
            tmp += '+' + str(lst[i])
        answer.append(tmp)
        return
    
    for i in range(1, 4):
        recur(lst + [i])

    return

N, k = map(int, input().split())
answer = []
recur([])
answer.sort()
if k <= len(answer):
    print(answer[k-1])
else:
    print(-1)
