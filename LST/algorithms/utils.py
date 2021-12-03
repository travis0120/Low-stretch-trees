import LST as lst

__all__ = ['contract_nodes',
           'compose_graph']


def contract_nodes(graph, u, v, self_loops=True):
    H = graph

    v_nbrs = H.adj[v]
    v_edges_remap = [(v, nbr, data) for nbr, data in v_nbrs.items()]

    v_data = H.nodes[v]
    H.remove_node(v)

    for (prev_w, prev_x, d) in v_edges_remap:
        w = prev_w if prev_w != v else u
        x = prev_x if prev_x != v else u

        if ({prev_w, prev_x} == {u, v}) and not self_loops:
            continue

        if not H.has_edge(w, x):
            H.add_edge(w, x, **d)
        else:
            if "contraction" in H.edges[(w, x)]:
                H.edges[(w, x)]["contraction"][(prev_w, prev_x)] = d
            else:
                H.edges[(w, x)]["contraction"] = {(prev_w, prev_x): d}

    if "contraction" in H.nodes[u]:
        H.nodes[u]["contraction"][v] = v_data
    else:
        H.nodes[u]["contraction"] = {v: v_data}
    return H


def compose_graph(graph_a, graph_b):
    H = lst.Graph()
    a_adj, b_adj = graph_a.adj, graph_b.adj
    H.add_edges_from((u, v, data) for u, nbrs in a_adj.items() for v, data in nbrs.items())
    H.add_edges_from((u, v, data) for u, nbrs in b_adj.items() for v, data in nbrs.items())
    return H
