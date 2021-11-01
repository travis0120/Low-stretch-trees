import networkx as nx
import numpy as np

__all__ = ['all_paris_shortest_path',
           'shortest_path']


def _dijkstra(graph, vertex, cutoff=None):
    """
    :param graph:
    :param vertex:
    :return:
    """

    G = graph
    seen = {}
    level = 0
    next_level = set(vertex)
    n = len(G)
    if cutoff is None:
        cutoff = float('inf')

    while next_level and cutoff > level:
        this_level = next_level
        next_level = set()
        found = []
        for v in this_level:
            if v not in seen:
                seen[v] = level
                found.append(v)
                yield v, level
        if len(seen) == n:
            return
        for v in found:
            next_level.update(G[v])
        level += 1
    del seen


def shortest_path(graph, target, cutoff=None):
    # if not isinstance(G, dict):
    #     raise ValueError("Only Accept Adjacency dict")
    first_level = {target: 1}
    return _dijkstra(graph, first_level, cutoff)


def all_paris_shortest_path(graph, cutoff=None):
    for n in graph:
        yield n, shortest_path(graph, n, cutoff)


def get_distance_between(graph, vertex_u, vertex_v):
    g, u, v = graph, vertex_u, vertex_v
    if u not in graph:
        raise BaseException(f"Can't find vertex {u} in Graph")
    if v not in graph:
        raise BaseException(f"Can't find vertex {v} in Graph")
    _distances_from = dict(shortest_path(g, u))
    return _distances_from[v]


def get_vertices_in_distance(graph, vertex, distance: int):
    g, u, i = graph, vertex, distance + 1
    _vertices = shortest_path(g, u, cutoff=i)
    return dict(_vertices)


#
def get_edges_in_distance(graph, vertex, distance: int, endpoints = 2):
    g, u, i = graph, vertex, distance + 1
    # _vertices = shortest_path(g, u, cutoff=i)

    seen = dict()
    level = 0
    next_level = set({vertex})
    n = len(g)
    ans = []
    seen = []
    while next_level and distance > level:
        this_level = next_level
        next_level = set()
        found = []

        for v in this_level:
            found.append(v)
        print('Found: ',found, 'Seen', seen)

        for v in found:
            print(v, [*g[v]])
            next_level.update(g[v])
        print("this: ", this_level, "next: ", next_level)
        print()
        level += 1
    return ans


def get_diameter(graph):
    all_shortest_path = all_paris_shortest_path(graph)
    _diameter = 0
    for _, distance in all_shortest_path:
        cur_max_distance = max(dict(distance).values())
        if cur_max_distance > _diameter:
            _diameter = cur_max_distance
    return _diameter


graph_edges = [(2, 1), (3, 1), (4, 1), (5, 1),
               (7, 6), (8, 6), (9, 6),
               (11, 10), (12, 10), (13, 10), (14, 10),
               (2, 9), (8, 11), (3, 14), (4, 13)]

G = nx.Graph(graph_edges)
a = shortest_path(G.adj, 1, 3)
# print(dict(a))

# print(get_vertices_in_distance(G.adj, 1, 3))

# not (6,7), (6,8),(8,11),(10, 11) (10,12)
a = get_edges_in_distance(G.adj, 1, 3)
print(a)