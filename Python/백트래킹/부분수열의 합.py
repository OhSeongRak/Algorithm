import sys
input = sys.stdin.readline

def recur(cnt, hab):
    global answer

    if cnt == N:
        if hab == S:
            answer += 1
        return
    
    recur(cnt+1, hab + lst[cnt])
    recur(cnt+1, hab)

    return

N, S = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0
recur(0, 0)
print(answer if S != 0 else answer - 1)