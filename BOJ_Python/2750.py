import sys

read = sys.stdin.readline
N = int(input())
list = [int(read().strip()) for _ in range(N)]

for i in range(N-1):
	min_idx = i
	for j in range(i+1, N):
		if list[min_idx] > list[j]:
			min_idx = j
	list[min_idx], list[i] = list[i], list[min_idx]

for i in list:
	print(i)