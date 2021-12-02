# from undirected import get_edges_in_distance
import networkx as nx

from LST.algorithms.undirected import *

__all__ = ['low_stretch_tree']


def generate_sub(adj, root):
    next_level = {root}
    seen = {root}
    tree_graph = nx.Graph()
    while next_level:
        this_level = next_level
        next_level = set()
        found = []

        for v in this_level:
            for u in adj[v]:
                if u not in seen:
                    found.append(u)
                    tree_graph.add_edge(v, u)

        for v in found:
            seen.add(v)
            next_level.add(v)
    del seen
    return tree_graph


def shortest_path_tree(graph_adj, partition):
    root = None
    min_d = float('inf')
    for v in partition:
        temp = dict(shortest_path(graph_adj, v)).values()
        if sum(temp) < min_d:
            root = v
            min_d = sum(temp)
    return generate_sub(graph_adj.copy(), root), root


def get_internal_and_inter_cluster(graph, partition):
    partition_adj = dict()
    outside_partition_adj = dict()
    for v in partition:
        for key, value in graph.adj[v].items():
            if key in partition:
                if v not in partition_adj.keys():
                    partition_adj[v] = dict()
                partition_adj[v].update({key: value})
            else:
                if v not in outside_partition_adj.keys():
                    outside_partition_adj[v] = dict()
                outside_partition_adj[v].update({key: value})
    return partition_adj, outside_partition_adj


def build_cluster(graph, c, a):
    limit = get_diameter(graph.adj)
    for node in graph.nodes:
        i = 1
        while i <= limit:
            distance_i_1 = get_edges_in_distance(graph, node, i + 1)
            distance_i = get_edges_in_distance(graph, node, i)
            _d_1, _d = len(tuple(distance_i_1)), len(tuple(distance_i)) * (1 + a)
            if _d_1 < _d:
                vertices = get_vertices_in_distance(graph, node, i)
                return list(vertices)
            i += 1
    return list(graph.nodes)


def build_partition(graph, c, D):
    import math
    g = graph.copy()
    C = g.number_of_edges()
    alpha = 4 * math.log(C) / D
    if alpha >= 1:
        yield list(graph)
    else:
        while g:
            _vs = build_cluster(g, c, alpha)
            g.remove_nodes_from(_vs)
            yield _vs


def low_stretch_tree(graph, c=None):
    C = graph.number_of_edges()
    D = get_diameter(graph)
    if D == 0:
        return graph
    _U = build_partition(graph, c, D)
    H = nx.Graph()
    while True:
        try:
            partition = next(_U)
            inside_adj, outside_adj = get_internal_and_inter_cluster(graph, partition)
            _spt, _root = shortest_path_tree(inside_adj, partition)
            _sub_G = nx.compose(_spt, nx.Graph(outside_adj))
            _sub_G.update(outside_adj)
            for v in inside_adj:
                if v != _root:
                    _sub_G = nx.contracted_nodes(_sub_G, _root, v)

            H.update(_sub_G)
        except StopIteration:
            break
    return low_stretch_tree(H)
