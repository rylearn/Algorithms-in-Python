
def generate_pascal_traingle(n):
    triangle_list = []
    arr = [1]
    triangle_list.append(arr)
    for i in range(1, n):
        arr = [1]
        for j in range(1, i):
            prev_arr = triangle_list[i - 1]
            arr.append(prev_arr[j - 1] + prev_arr[j])
        arr.append(1)
        triangle_list.append(arr)
    return triangle_list

res = generate_pascal_traingle(5)
for curr_arr in res:
    print(curr_arr)