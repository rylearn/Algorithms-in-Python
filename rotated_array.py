
def twod_rotation(arr):
    assert len(arr) == len(arr[0])
    copied_arr = [[0 for i in range(len(arr))] \
                  for j in range(len(arr))]

    n = len(arr)
    for i in range(n):
        vec = reversed([arr[j][i] for j in range(n)])
        copied_arr[i] = list(vec)
    return copied_arr

arr = [[3, 4], [1, 2]]
for i in range(len(arr)):
    print(arr[i])

res = twod_rotation(arr)
for i in range(len(res)):
    print(res[i])
