import sys

# start in the middle, move left
# find indices associated with maximum left sum
# start in the middle, move right
# find indices associated with maximum right sum
def find_max_crossing_subarray(A, low, mid, high):
	def get_index(start_range, end_range, incr):
		current_sum = 0
		final_sum = -sys.maxint
		final_index = -1
		for i in range(start_range, end_range, incr):
			current_sum += A[i]
			if current_sum > final_sum:
				final_sum = current_sum
				final_index = i
		return (final_index, final_sum)
	left_index, left_sum = get_index(mid, low, -1)
	right_index, right_sum = get_index(mid + 1, high + 1, 1)
	return (left_index, right_index, left_sum + right_sum)

def find_max_subarray(A, low = 0, high = -1):
	if high == -1:
		high = len(A) - 1
	if low == high:
		return (low, high, A[low])

	mid = (low + high) / 2
	(left_low, left_high, left_amount) = \
		find_max_subarray(A, low, mid)
	(right_low, right_high, right_amount) = \
		find_max_subarray(A, mid + 1, high)
	(cross_low, cross_high, cross_amount) = \
		find_max_crossing_subarray(A, low, mid, high)
	if left_amount > right_amount and left_amount > cross_amount:
		return (left_low, left_high, left_amount)
	elif right_amount > left_amount and right_amount > cross_amount:
		return (right_low, right_high, right_amount)
	else:
		return (cross_low, cross_high, cross_amount)
	
A = [-1, 2, 3, 13, 123, -23, -232, 132, -242]
low, high, amt = find_max_subarray(A, 0, len(A) - 1)
print(amt)

