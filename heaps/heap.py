
import sys
import copy

class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.heap_size = len(self.arr)

    def parent(self, i):
        if i == 0:
            return None
        return (i + 1) // 2 - 1

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def max_heapify(self, i, arr = None):
        if arr != None:
            self.arr = arr
            self.heap_size = len(self.arr)
        l = self.left(i)
        r = self.right(i)
        A = self.arr
        if l < self.heap_size and \
            A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and \
            A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(largest, A)

    def build_max_heap(self, arr = None):
        if arr != None:
            self.arr = arr
            self.heap_size = len(arr)
        A = self.arr
        for i in range(len(A) - 1, -1, -1):
            self.max_heapify(i, A)

    def heapsort(self, arr = None):
        if arr != None:
            self.arr = arr
            self.heap_size = len(arr)
        A = self.arr
        self.build_max_heap()
        for i in range(len(A)-1, 0, -1):
            A[0], A[i] = A[i], A[0]
            self.heap_size -= 1
            self.max_heapify(0, A)

def heapsort(arr):
    heap_object = Heap(arr)
    heap_object.heapsort()

class PriorityQueue:

    def __init__(self, arr = None):
        self.heap_object = Heap(arr)
        self.heap_object.build_max_heap()

    def heap_maximum(self):
        return self.heap_object.arr[0]

    def heap_extract_max(self):
        if self.heap_object.heap_size < 1:
            raise Exception('Heap underflow')
        max_val = self.heap_object.arr[0]

        ind = self.heap_object.heap_size - 1
        self.heap_object.arr[0] = self.heap_object.arr[ind]

        del self.heap_object.arr[ind]
        self.heap_object.heap_size -= 1

        self.heap_object.max_heapify(0)
        return max_val

    def heap_increase_key(self, i, key):
        if key < self.heap_object.arr[i]:
            raise Exception('Key smaller')
        A = self.heap_object.arr
        A[i] = key
        # parent_ind = self.heap_object.parent(i)
        while i > 0 and A[self.heap_object.parent(i)] < A[i]:
            A[i], A[self.heap_object.parent(i)] = A[self.heap_object.parent(i)], A[i]
            i = self.heap_object.parent(i)

    def max_heap_insert(self, key):
        self.heap_object.heap_size += 1
        ind = self.heap_object.heap_size - 1
        self.heap_object.arr.append(float('-inf'))
        self.heap_increase_key(ind, key)

A = [5, 13, 2, 25, 2, 17, 20, 24, 8]
p_queue = PriorityQueue(A)
print(p_queue.heap_maximum())
print(p_queue.heap_object.arr)
print(p_queue.heap_extract_max())
print(p_queue.heap_object.arr)
print(p_queue.heap_extract_max())
print(p_queue.heap_object.arr)
p_queue.heap_increase_key(2, 18)
print(p_queue.heap_object.arr)
p_queue.max_heap_insert(28)
print(p_queue.heap_object.arr)
print(p_queue.heap_extract_max())
print(p_queue.heap_object.arr)
for i in range(len(p_queue.heap_object.arr) - 2):
    print(p_queue.heap_extract_max(), end = ' ')
