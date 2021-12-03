import random

import LST as lst

__all__ = ['random_mst']


def random_mst(graph):
    def find(parent, v):
        if parent[v] == v:
            return v
        return find(parent, parent[v])

    n_nodes = graph.number_of_nodes()
    n_edges = graph.number_of_edges()

    edges_lst = list(graph.edges)
    _rw = [random.randint(1, n_edges + 1) for _ in range(n_edges)]
    rank_edges = [x for x, _ in sorted(zip(edges_lst, _rw), key=lambda pair: pair[1])]

    parents_map = dict()
    for v in graph.nodes:
        parents_map[v] = v

    e_count = 0
    e_index = 0
    result = []
    while e_count < n_nodes - 1:
        u, v = rank_edges[e_index]
        e_index += 1

        x, y = find(parents_map, u), find(parents_map, v)
        if x != y:
            e_count += 1
            result.append((u, v))
            parents_map[x] = y

    H = lst.Graph()
    for u, v in result:
        H.add_edge(u, v)
    return H
