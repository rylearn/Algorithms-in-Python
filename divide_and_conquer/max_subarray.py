import sys

def find_max_cross_subarray(A, low, mid, high):
	left_cross = 0
	left_index = None
	left_max = -sys.maxint - 1
	for i in range(mid, -1, -1):
		left_cross += A[i]
		if left_cross > left_max:
			left_max = left_cross
			left_index = i

	right_cross = 0
	right_max = -sys.maxint - 1
	for i in range(mid + 1, high + 1):
		right_cross += A[i]
		if right_cross > right_max:
			right_max = right_cross
			right_index = i

	return (left_index, right_index, \
		left_max + right_max)

def find_max_subarray(A, low, high):
	if low == high:
		return (low, high, A[low])
	else:
		mid = (low + high) / 2
		left_low, left_high, left_sum = \
			find_max_subarray(A, low, mid)
		right_low, right_high, right_sum = \
			find_max_subarray(A, mid + 1, high)
		cross_low, cross_high, cross_sum = \
			find_max_cross_subarray(A, low, mid, high)
		if left_sum >= right_sum and \
			left_sum >= cross_sum:
			return (left_low, left_high, left_sum)
		elif right_sum >= left_sum and \
			right_sum >= cross_sum:
			return (right_low, right_high, right_sum)
		else:
			return (cross_low, cross_high, cross_sum)

A = [4, -1, 5, -1, 10]
res = find_max_subarray(A, 0, len(A) - 1)
print res[2]
