from multiprocessing import Pool
import time

def f(x):
	return x*x

if __name__ == '__main__':
	here = time.clock()
	p = Pool(5)
	print(p.map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
	here2 = time.clock()
	print here2 - here

	here = time.clock()
	print "%d %d %d" %(f(1), f(2), f(3))
	here2 = time.clock()
	print here2 - here
