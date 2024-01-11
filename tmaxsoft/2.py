import sys
from itertools import permutations
input = sys.stdin.readline


def solution(letters):
    lst = sorted(list(letters))
    N = len(lst)
    answer = []

    for letter in list(permutations(lst, N)):
        for i in range(1, len(letter)):
            if letter[i] == letter[i - 1]:
                break
        else:
            answer.append(''.join(letter))

    # answer = list(answer)
    # answer.sort()
    return answer


letters = "abca"
print(solution(letters))