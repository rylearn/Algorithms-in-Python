#include <vector>
#include <iostream>
using namespace std;

void swap(int& x, int& y) {
	int temp = x;
	x = y;
	y = temp;
}

int partition(vector<int>& A, int p, int r) ;

void quicksort(vector<int>& A, int p, int r) {
	if (p < r) {
		int q = partition(A, p, r);
		quicksort(A, p, q - 1);
		quicksort(A, q + 1, r);
	}
}

int partition(vector<int>& A, int p, int r) {
	int x = A[r];
	int i = p - 1;
	for (int j = p; j <= r - 1; ++ j) {
		if (A[j] <= x) {
			i += 1;
			swap(A[i], A[j]);
		}
	}
	swap(A[i+1], A[r]);
	return i + 1;
}

int main() {
	vector<int> x {5234, 34,234, 2, 12340, 2};
	quicksort(x, 0, 5);
	for (int i: x) {
		cout << i << endl;
	}
	return 0;
}
