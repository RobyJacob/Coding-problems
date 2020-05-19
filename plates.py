def beauty(idx, taken):
    if taken == P:
        return 0
    if idx > N or taken > P:
        return -1e9

    if cache[idx][taken] != -1:
        return cache[idx][taken]

    ans = -1e9
    for i in range(K+1):
        ans = max(ans, pref[idx][i] + beauty(idx + 1, taken + i))
    cache[idx][taken] = ans

    return cache[idx][taken]

t = int(input())

for tc in range(t):
    N, K, P = list(map(int, input().split()))

    stacks = [[0 for _ in range(K+1)] for _ in range(N+1)

    for i in range(1, N+1):
        stacks[i][1:] = list(map(int, input().split()))

    # print(stacks)
    pref = [[0 for _ in range(K+1)] for _ in range(N+1)]
    cache = [[-1 for _ in range((N+1)*K)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            pref[i][j] = pref[i][j-1] + stacks[i][j]

    ans = beauty(1, 0)

    print("Case #{}: {}".format(tc+1, ans))
