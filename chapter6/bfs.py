#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

# Breadth first search
search_q = deque()
already_checked = {}
# 1. Keep a queue of people to check
search_q += graph['you']
# 2. Pop a person off the queue
while search_q:
    elem = search_q.popleft()
    if already_checked.get(elem):
        continue
    already_checked[elem] = True
    print('Checking', elem, '...')
    if person_is_seller(elem):
        # We found the seller!
        print('The closest mango seller is', elem, '!!!')
        break
    else:
        # Add all neighbors of that person
        search_q += graph[elem]
