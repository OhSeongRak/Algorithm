N, M = 3, 4
# for i in range(1 << N * (M-1)):
#     for j in range(N * (M-1)):
#         if i & (1 << j):
#             print(j // (M-1), j % (M-1))


# for j in range(N * (M-1)):
#     print(j // (M-1), j % (M-1))

for l in range((N-1) * M):
    print(l // M, l % M)
    # 겹치면 안됨
    # if k & (1 << l) and right[j // (M-1)][j % (M-1)] == False: