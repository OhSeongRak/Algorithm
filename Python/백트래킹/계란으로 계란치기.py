import sys
input = sys.stdin.readline

def recur(cur):
    global ans

    if cur == N:
        cnt = 0
        for i in range(N):
            if eggs[i][0] <= 0:
                cnt += 1
        ans = max(ans, cnt)
        return
    
    if eggs[cur][0] <= 0: # 현재 위치의 계란이 깨져있다면
        recur(cur+1)
        return

    for i in range(N):
        if eggs[i][0] <= 0 or i == cur:
            continue

        # 계란으로 계란치기
        eggs[cur][0] -= eggs[i][1]
        eggs[i][0] -= eggs[cur][1]
        recur(cur + 1)
        eggs[cur][0] += eggs[i][1]
        eggs[i][0] += eggs[cur][1]

    cnt = 0
    for i in range(N):
        if eggs[i][0] <= 0:
            cnt += 1
    ans = max(ans, cnt)
    return

N = int(input())
eggs, ans = [], 0
for _ in range(N):
    eggs.append(list(map(int, input().split())))

recur(0)
print(ans)