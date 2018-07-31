
def fib(n, cache = {}):
	if n == 0:
		return 0
	if n <= 2:
		return 1
	if n in cache:
		return cache[n]
	else:
		data = fib(n - 1, cache) + fib(n - 2, cache)
		cache[n] = data
		return cache[n]

def fib_iterative(n):
	arr = [0 for i in range(n + 1)]
	arr[0] = 0
	arr[1] = 1
	for i in range(2, n + 1):
		arr[i] = arr[i - 1] + arr[i - 2]
	return arr[n]

n = 10000
# print fib(n)
print fib_iterative(n)
