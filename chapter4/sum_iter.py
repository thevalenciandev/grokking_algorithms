#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum_iter(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum


print(sum_iter([1, 2, 3]))
