import sys
from collections import deque
input = sys.stdin.readline


def solution():
    if sum(lst) % 3 != 0:
        return 0
    
    queue = deque([lst])
    while queue:
        tmp = queue.popleft()
        tmp.sort()
        e1, e2, max_ = tmp
        
        if e1 == e2 == max_:
            return 1
        
        if (e1, e2, max_) in visited:
            continue
        
        visited.add((e1, e2, max_))
        queue.append([max_ - e1, e2, e1 * 2])
        queue.append([max_ - e2, e2 * 2, e1])
    
    return 0

lst = list(map(int, input().split()))
visited = set()
print(solution())