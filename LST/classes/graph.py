from .view import AdjacencyView, EdgeView

__all__ = ['Graph']


class Graph(object):
    node_dict = dict
    adj_outer_dict_factory = dict
    adj_inner_dict_factory = dict
    edge_attr_dict_factory = dict

    def __init__(self, edges_data=None):
        self._nodes = self.node_dict()
        self._adj = self.adj_outer_dict_factory()
        if edges_data and isinstance(edges_data, list):
            self.add_edges_from(edges_data)

    def __len__(self):
        return len(self._nodes)

    def __contains__(self, item):
        try:
            return item in self._nodes
        except ValueError:
            return False

    def __getitem__(self, item):
        return self._adj[item]

    @property
    def nodes(self):
        return self._nodes

    @property
    def edges(self):
        return EdgeView(self)
        # return self._adj

    @property
    def adj(self):
        return AdjacencyView(self._adj)
        # return self._adj

    def add_node(self, node_name):
        if node_name not in self._nodes:
            if node_name is None:
                raise ValueError('None cannot be a Node!')
            self._adj[node_name] = self.adj_inner_dict_factory()
            self._nodes[node_name] = self.node_dict()

    def add_edge(self, edge_u, edge_v, **attr):
        u, v = edge_u, edge_v
        if u not in self._nodes:
            if u is None:
                raise ValueError('None cannot be a Node!')
            self._adj[u] = self.adj_inner_dict_factory()
            self._nodes[u] = self.node_dict()

        if v not in self._nodes:
            if v is None:
                raise ValueError('None cannot be a Node!')
            self._adj[v] = self.adj_inner_dict_factory()
            self._nodes[v] = self.node_dict()

        datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
        datadict.update(attr)
        self._adj[u][v] = datadict
        self._adj[v][u] = datadict

    def add_edges_from(self, brunch_of_edge):
        for e in brunch_of_edge:
            len_e = len(e)
            if len_e == 2:
                u, v = e
                attr = {}
            else:
                raise Exception(f"Edge tuple {e} must be a 2-tuple")
            self.add_edge(u, v, *attr)

    def adjacency(self):
        return iter(self._adj.items())

    def is_multigraph(self):
        return False

    def number_of_nodes(self):
        return len(self._nodes)

    def number_of_edges(self):
        return len(self.edges)
