import sys
input = sys.stdin.readline


def recur(cnt, dup, numbers):
    global answer

    if dup == 2:
        return
    
    if cnt == 10:
        score = 0
        for i in range(10):
            if numbers[i] == lst[i]:
                score += 1
        
        if score >= 5:
            answer += 1
        return
    
    for i in range(1, 6):
        if len(numbers) != 0 and numbers[-1] == i:
            recur(cnt + 1, dup + 1, numbers + [i])
        else:
            recur(cnt + 1, 0, numbers + [i])


    return

answer = 0
lst = list(map(int, input().split()))
recur(0, 0, [])
print(answer)