import sys, bisect
input = sys.stdin.readline

def solution():
    global bags
    ans = 0

    for weight, value in jewels:
        if len(bags) == 0:
            break

        if weight > bags[-1]:
            continue

        idx = bisect.bisect_left(bags, weight)
        ans += value
        del bags[idx]

    return ans

N, K = map(int, input().split())
jewels, bags = [], []
for _ in range(N):
    jewels.append(list(map(int, input().split())))

for _ in range(K):
    bags.append(int(input()))

bags.sort()
jewels.sort(key=lambda jewel : -jewel[1])
print(solution())

# 가방에는 보석 1개만 넣을 수 있음
# 정렬해서 할까? 보석을 가치순으로 정렬
# 가방은 최대 용량순으로 정렬
# 보석이 가방에 못드감, 넘어감
# 드갈 수 있음