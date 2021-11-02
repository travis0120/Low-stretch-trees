import collections
import networkx as nx

__all__=['all_paris_shortest_path',
         'shortest_path',
         'get_edges_in_distance',
         'get_vertices_in_distance',
         'get_distance_between',
         'get_diameter']


def _dijkstra(graph, vertex, cutoff):
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
    if cutoff is None:
        cutoff = float('inf')
    return _dijkstra(graph, first_level, cutoff)


def all_paris_shortest_path(graph, cutoff=None):
    for n in graph:
        yield n, dict(shortest_path(graph, n, cutoff))


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


def get_edges_in_distance(graph, vertex, distance: int, endpoints = 2):
    g, u, i = graph, vertex, distance + 1

    level = 0
    next_level = set({vertex})
    n = len(g)

    seen = collections.defaultdict(list)
    while next_level and distance > level:
        this_level = next_level
        next_level = set()
        found = []

        for v in this_level:
            found.append(v)

        for v in found:
            for u in g[v]:
                if u not in seen[v]:
                    yield v, u
                seen[v].append(u)
                seen[u].append(v)

            next_level.update(g[v])
        level += 1
    del seen


def get_diameter(graph):
    all_shortest_path = all_paris_shortest_path(graph)
    _diameter = 0
    for _, distance in all_shortest_path:
        cur_max_distance = max(dict(distance).values())
        if cur_max_distance > _diameter:
            _diameter = cur_max_distance
    return _diameter
