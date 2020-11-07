def binary_search(item, list):
    return binary_search_helper(item, list, 0, len(list)-1)


def binary_search_helper(item, list, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    guess = list[mid]
    if item < guess:
        return binary_search_helper(item, list, low, mid-1)
    elif item > guess:
        return binary_search_helper(item, list, mid+1, high)
    else:
        return mid
        

def binary_search_2(item, list):
    low = 0
    high = len(list) - 1

    while low<=high:
        mid = (low + high) // 2
        guess = list[mid]
        if item < guess:
            high = mid - 1
        elif item > guess:
            low = mid + 1
        else:
            return mid
    mid = (low + high) // 2

    return None


my_list   = [1, 2, 3, 7, 9, 11]
my_list_2 = [1, 2, 7, 9, 11]
print(binary_search(0, my_list))
print(binary_search(1, my_list))
print(binary_search(2, my_list))
print(binary_search(3, my_list))
print(binary_search(7, my_list))
print(binary_search(9, my_list))
print(binary_search(11, my_list))
print(binary_search(21, my_list))
print(binary_search(7, my_list_2))
print(binary_search(9, my_list_2))
print(binary_search(11, my_list_2))
print(binary_search(12, my_list_2))
