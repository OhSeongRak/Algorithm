import sys

input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


A = list(map(int, input().split()))
B = list(map(int, input().split()))
GCD = gcd(A[1], B[1])
ja = A[0] * (B[1] // GCD) + B[0] * (A[1] // GCD)
mo = A[1] * B[1] // GCD

GCD = gcd(ja, mo)
print(ja // GCD, mo // GCD)
