#!/usr/bin/python3

import sys

'''
Generate powerset of a given set.
For eg:- powerset([1,2,3]) = [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
'''

def powerset(arr):
	if len(arr) == 0:
		return [arr]
	return powerset(arr[:-1]) + [el + [arr[-1]] for el in powerset(arr[:-1])]

def main():
	if len(sys.argv) < 2:
		print("Please specify arguments as sequence of numbers seperated by space")
		sys.exit(1)

	arr = list(map(int, sys.argv[1:]))

	print(powerset(arr))

if __name__ == "__main__":
	main()
