def check(dopt):
    cnt = 0
    for i in range(N-1):
        di = arr[i+1] - arr[i]
        addsess = int((di-1) / dopt)
        cnt += addsess
        if cnt > K:
            return False

    return True

def bsearch(lo, hi):
    if lo == hi:
        return lo

    mid = int((lo + hi) / 2)

    if check(mid):
        return bsearch(lo, mid)
    else:
        return bsearch(mid+1, hi)

t = int(input())
for tc in range(t):
    N, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    ans = bsearch(1, 10**9)
    print("Case #{}: {}".format(tc+1, ans))
