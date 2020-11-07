#!/usr/bin/env python
# -*- coding: utf-8 -*-

def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        # 1. choose a pivot
        pivot = arr[0]
        # 2. partition array
        left, right = partition(arr, pivot)
        # 3. recursively call quicksort
        return qsort(left) + [pivot] + qsort(right)


def partition(arr, pivot):
    left = []
    right = []
    for i in range(1, len(arr)):
        elem = arr[i]
        if elem <= pivot:
            left.append(elem)
        else:
            right.append(elem)
    return left, right


my_arr_1 = []
my_arr_2 = [1]
my_arr_3 = [1, 7]
my_arr_4 = [7, 1]
my_arr_5 = [1, 2, 4]
my_arr_6 = [2, 4, 1]
my_arr_7 = [2, 4, 1, 0, 6]
print(qsort(my_arr_1))
print(qsort(my_arr_2))
print(qsort(my_arr_3))
print(qsort(my_arr_4))
print(qsort(my_arr_5))
print(qsort(my_arr_6))
print(qsort(my_arr_7))
