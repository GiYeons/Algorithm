# 버블 정렬 Bubble Sort
list = list(map(int, input().split()))

for i in range(len(list) - 1, 0, -1):
	for j in range(i):
		if list[j] > list[j+1]:
			list[j], list[j+1] = list[j+1], list[j]
			
print(*list)


# Sort 함수 사용
list = list(map(int, input().split()))
list.sort()
print(*list)


# 선택 정렬 Selection Sort 1
list = list(map(int, input().split()))

for i in range(len(list)-1):
	for j in range(i+1, len(list)):
		if list[i] > list[j]:
			list[i], list[j] = list[j], list[i]

print(*list)

# 선택 정렬 Selection Sort 2
list = list(map(int, input().split()))

for i in range(len(list) - 1):
	min_idx = i
	for j in range(i+1, len(list)):
		if list[min_idx] > list[j]:
			min_idx = j
	list[min_idx], list[i] = list[i], list[min_idx]
		
print(*list)