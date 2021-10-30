import networkx as nx

__all__=['all_paris_shortest_path',
         'shortest_path']

def _dijkstra(graph, vertex,cutoff):
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


def shortest_path(G, target, cutoff=None):
    # if not isinstance(G, dict):
    #     raise ValueError("Only Accept Adjacency dict")
    first_level = {target: 1}
    if cutoff is None:
        cutoff = float('inf')
    return _dijkstra(G, first_level, cutoff)


def all_paris_shortest_path(G, cutoff=None):
    for n in G:
        yield n, dict(shortest_path(G, n, cutoff))


def vecters_in_distances(G, scr, cutoff=None):
    vecters = dict(shortest_path(G, scr, cutoff))
    return vecters
