#!/usr/bin/python3

import sys

def lis(arr):
    n = len(arr)

    l = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and l[i] < l[j] + 1:
                l[i] = l[j] + 1

    return max(l)

def main():
    if len(sys.argv) < 2:
        print("Please specify arguments as numbers seperated by space")
        sys.exit(1)

    nums = list(map(int, sys.argv[1:]))
    print(lis(nums))

if __name__ == "__main__":
    main()
