#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum_rec(arr):
    return sum_rec_helper(arr, len(arr)-1)


def sum_rec_helper(arr, i):
    if i == 0:
        return arr[i]
    else:
        return arr[i] + sum_rec_helper(arr, i-1)


print(sum_rec([1, 2, 3]))
