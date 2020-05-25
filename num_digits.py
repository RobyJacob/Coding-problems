def solve(n):
    cnt = 0
    i = 1

    while i <= n:
        cnt += (n - i + 1)
        i *= 10

    return cnt


def main():
    n = int(input())

    print(solve(n))


if __name__ == "__main__":
    main()
