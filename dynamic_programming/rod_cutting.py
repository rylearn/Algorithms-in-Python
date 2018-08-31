
def memoized_cut_rod(p, n):
    r = [0 for i in range(n + 1)]
    s = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        q = float('-inf')
        for j in range(1, i + 1):
            if q < p[j - 1] + r[i - j]:
                q = p[j - 1] + r[i - j]
                s[i] = j
        r[i] = q
    return r, s

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = len(prices)
r, s = memoized_cut_rod(prices, n)
print(r)
print(s)
