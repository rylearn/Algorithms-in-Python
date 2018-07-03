import sys

def insertion_sort(A):
	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i + 1] = A[i]
			i -= 1
		A[i + 1] = key

def swap(A, index1, index2):
	temp = A[index1]
	A[index1] = A[index2]
	A[index2] = temp

def bubble_sort(A):
	for i in range(0, len(A) - 1):
		for j in range(len(A) - 1, i, -1):
			if A[j] < A[j - 1]:
				swap(A, j, j - 1)

def merge_sort(A, first_index = 0, last_index = -1):
	if last_index == -1:
		last_index = len(A) - 1
	if first_index < last_index:
		mid_index = (first_index + last_index) / 2
		merge_sort(A, first_index, mid_index)
		merge_sort(A, mid_index + 1, last_index)
		merge(A, first_index, mid_index, last_index)


def merge(A, first_index, mid_index, last_index):
	length1 = mid_index - first_index + 1 	# mid index in first partition
	length2 = last_index - mid_index
	L = [0 for i in range(length1 + 1)]
	R = [0 for i in range(length2 + 1)]
	for i in range(length1):
		L[i] = A[first_index + i]
	for i in range(length2):
		R[i] = A[mid_index + 1 + i]
	L[length1] = sys.maxint
	R[length2] = sys.maxint
	i = 0
	j = 0
	for k in range(first_index, last_index + 1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1

A = [3, 4, 2, 4, 9, 1, 2]
B = [2, 8, 29, 23, 11, 28, 48]
C = [2, 8, 29, 23, 11, 28, 48]
insertion_sort(A)
bubble_sort(B)
merge_sort(C)
print(A)
print(B)
print(C)

