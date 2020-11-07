#!/usr/bin/env python
# -*- coding: utf-8 -*-

def max_rec(arr):
    return max_rec_helper(arr, len(arr) - 1)


def max_rec_helper(arr, i):
    if i == 0:
        return arr[i]
    else:
        return max(arr[i], max_rec_helper(arr, i-1))


a = [10, 6, 7]
print(max_rec(a))
