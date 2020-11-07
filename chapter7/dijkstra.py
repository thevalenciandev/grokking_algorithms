#!/usr/bin/env python
# -*- coding: utf-8 -*-


def generate_dijkstra_graph(g):
    # Build graph
    graph = {}
    costs = {}
    parents = {}
    nodes_and_weights = g.split('|')
    for n in nodes_and_weights:
        node_and_neighbors = n.split(':')
        node = node_and_neighbors[0]
        graph[node] = {}
        costs[node] = float('inf')
        parents[node] = None
        if len(node_and_neighbors) == 1:  # Must be the last node
            continue
        neighbors = node_and_neighbors[1]
        for nb in neighbors.split(','):
            nh = nb.split('=')
            n = nh[0]
            cost = int(nh[1])
            graph[node][n] = cost

    # Populate initial values for costs and parents
    # TODO: START and FIN shouldn't be hardcoded
    for n, c in graph['START'].items():
        costs[n] = c
        parents[n] = 'START'
    costs['FIN'] = float('inf')
    parents['FIN'] = None

    # Build
    return graph, costs, parents


def find_lowest_cost_node(costs, processed):
    lo = float("inf")  # infinity
    nd = None
    for n, c in costs.items():
        if c < lo and n not in processed:
            lo = c
            nd = n
    return nd


def get_shortest_weighted_path():
    path = []
    pt = 'FIN'
    while pt != 'START':
        path.append(pt)
        pt = parents[pt]
    path.append('START')
    return path


def dijkstra_algo(graph, costs, parents):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        print('Next lowest node is', node, 'now, with cost', cost)
        for nb, nbc in graph[node].items():  # for all the neighbors of node...
            new_cost = cost + nbc  # calculate new cost via that node
            print('Going to', nb, 'via', node, 'costs', new_cost)
            if costs[nb] > new_cost:
                costs[nb] = new_cost  # we found a cheaper path, update cost
                parents[nb] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)


if __name__ == '__main__':
    # g = 'START:A=6,B=2|A:FIN=1|B:A=3,FIN=5|FIN'
    # g = 'START:A=5,B=2|A:C=4,D=2|B:A=8,D=7|C:FIN=3,D=6|D:FIN=1|FIN'
    g = 'START:A=10|A:C=20|B:A=1,C=1|C:FIN=30|FIN'
    graph, costs, parents = generate_dijkstra_graph(g)
    print('Graph:', graph)
    print('Costs:', costs)
    print('Parnt:', parents)

    dijkstra_algo(graph, costs, parents)

    path = get_shortest_weighted_path()
    cost_shortest_path = costs['FIN']
    print('Shortest path found', path, 'with cost', cost_shortest_path)
