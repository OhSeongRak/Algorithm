import sys
input = sys.stdin.readline

# cur: number의 길이
def ok(cur, number):
    k = 1
    while k < cur:
        # 끝에서 k개 == 끝에서 2k ~ k개면 나쁜수열
        if number[cur-k:] == number[cur-2*k:cur-k]:
            return False
        k += 1

    return True

def recur(cur, number):
    if cur == N+1:
        print(number)
        exit()
    
    for i in [1, 2, 3]:
        if len(number) == 0 or ok(cur, number + str(i)):
            recur(cur+1, number + str(i))

    return

N = int(input())
recur(1, '')