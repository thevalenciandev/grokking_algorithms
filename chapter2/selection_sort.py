def find_smallest(arr):
    if len(arr) == 0:
        return None
    index = 0
    smallest = arr[index]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            index = i
            smallest = arr[index]
    return index


def selection_sort(arr):
    res = []
    for i in range(0, len(arr)):
        smallest_index = find_smallest(arr)
        res.append(arr.pop(smallest_index))
    return res


arr_1 = []
arr_2 = [2]
arr_3 = [1, 2]
arr_4 = [2, 1]
print(find_smallest(arr_1))
print(find_smallest(arr_2))
print(find_smallest(arr_3))
print(find_smallest(arr_4))
print(selection_sort(arr_1))
print(selection_sort(arr_2))
print(selection_sort(arr_3))
print(selection_sort(arr_4))
