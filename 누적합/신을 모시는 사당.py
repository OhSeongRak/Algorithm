import sys
input = sys.stdin.readline

def solution():
    left , right, l_sum, r_sum = 0, 0, 0, 0
    for k in lst:
        if k == 1:
            left += 1
        else:
            right += 1
        l_sum = max(l_sum, left - right)
        r_sum = max(r_sum, right - left)

    return l_sum + r_sum

N = int(input())
lst = list(map(int, input().split()))
print(solution())