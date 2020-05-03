#!/usr/bin/python3

import sys
import math

'''
Given an array of N integers and a target value, find 3 numbers such that their sum is closest to the target
and return the sum
For eg:- input: [-1, 2, 1, -4] target = 1
        output: 2 (i.e., -1+2+1=2)
'''

def find_closest_sum(arr, target):
    closest_sum, min_diff = 0, math.inf
    arr.sort()
    for i in range(len(arr)-2):
        ptr1, ptr2 = i+1, len(arr)-1
        while ptr1 < ptr2:
            current_sum = arr[i] + arr[ptr1] + arr[ptr2]
            if min_diff > abs(current_sum-target):
                closest_sum = current_sum
                min_diff = abs(current_sum-target)
            if current_sum > target:
                ptr2 -= 1
            else:
                ptr1 += 1
    return closest_sum

def main():
    if len(sys.argv) < 2:
        print("Please specify arguments as space seperated numbers")
        sys.exit(-1)

    arr = list(map(int, sys.argv[1:]))

    t = int(input("Target value: "))

    print(find_closest_sum(arr, t))

if __name__ == "__main__":
    main()
