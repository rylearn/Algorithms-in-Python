
# O(n), assumes A has
# elements in range 0 to k inclusive
def counting_sort(A, k):
    C = [0 for i in range(k + 1)]
    B = []
    for j in range(len(A)):
        C[A[j]] += 1
    for i in range(k + 1):
        for j in range(C[i]):
            B.append(i)
    return B

def partition(A, p, r, ind):
    pivot = A[r] * pow(10, ind)
    i = p - 1
    for j in range(p, r):
        if A[j] * pow(10, ind) <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort_radix(A, p, r, i):
    if p < r:
        q = partition(A, p, r, i)
        quicksort_radix(A, p, q - 1, i)
        quicksort_radix(A, q + 1, r, i)

# start from lowest-order digit
# sort based on that
def radix_sort(A, d):
    for i in range(d):
        quicksort_radix(A, 0, len(A) - 1, i - 1)

def insertion_sort(A):
    i = 1
    while i < len(A):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
        i += 1

def bucket_sort(A):
    B = []
    n = len(A)
    for i in range(n):
        B.append([])
    for i in range(n):
        ind = int(n * A[i])
        B[ind].append(A[i])
    for i in range(n):
        insertion_sort(B[i])
    return sum(B, [])

# lst = [0, 12, 3, 11, 2, 3, 5, 4, 5, 1, 2]
# B = counting_sort(lst, 5)

lst = [0.1, 0.12, 0.3, 0.11, 0.2, 0.3, 0.5, 0.4, 0.5, 0.1, 0.2]
B = bucket_sort(lst)
print(B)
