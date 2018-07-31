
class Item:
	def __init__(self, weight, value):
		self.weight = weight
		self.value = value

def partition(list_items, p, r):
	pivot = A[r]
	i = p - 1
	for j in range(p, r, 1):
		if A[j] <= pivot:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i + 1], A[r] = A[r], A[i + 1]
	return i + 1

def sort_items(list_items, p = None, r = None):
	if p == None:
		p = 0
	if r == None:
		r = len(list_items) - 1
	if p < r:
		q = partition(list_items, p, r)
		sort_items(list_items, p, q - 1)
		sort_items(list_items, q + 1, r)

def recursive_knapsack(max_weight, weight_list, 
	n, value_list):
	if n == 0 or max_weight == 0:
		return 0

	# assumes weight list is ordered from 
	# smallest to largest
	if weight_list[n - 1] > max_weight:
		return knapsack(max_weight, weight_list,
			n - 1, value_list)

	else:
		return max(value_list[n - 1] + 
			recursive_knapsack(max_weight - weight_list[n - 1],
				weight_list, n - 1, value_list),
			recursive_knapsack(max_weight, weight_list, 
				n - 1, value_list))

def knapsack(max_weight, weight_list, 
	n, value_list):
	
	D_table = [[0 for i in range(max_weight + 1)] 
		for j in range(n + 1)]

	for i in range(n + 1):
		for w in range(max_weight + 1):
			if i == 0 or w == 0:
				D_table[i][w] = 0
			elif weight_list[i - 1] <= w:
				D_table[i][w] = max(
						value_list[i - 1] + 
						D_table[i - 1][w - weight_list[i - 1]],
						D_table[i - 1][w]
					)
			else:
				D_table[i][w] = D_table[i - 1][w]
	return D_table[n][max_weight]

items = [60, 100, 120]
weights = [10, 20, 30]
max_weight = 50
n = len(items)
print(knapsack(max_weight, weights, n, items))
print(recursive_knapsack(max_weight, weights, n, items))
