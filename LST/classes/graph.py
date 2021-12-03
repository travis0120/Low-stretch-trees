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
        elif edges_data and isinstance(edges_data, dict):
            self.add_edges_from(
                ((u, v, data) for u, nbrs in edges_data.items() for v, data in nbrs.items())
            )

    def __len__(self):
        return len(self._nodes)

    def __contains__(self, item):
        try:
            return item in self._nodes
        except ValueError:
            return False

    def __getitem__(self, item):
        return self._adj[item]

    def __iter__(self):
        return iter(self._nodes)

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

    def remove_node(self, n):
        adj = self._adj
        try:
            nbrs = list(adj[n])
            del self._nodes[n]
        except KeyError as err:
            raise ValueError(f"The node {n} is not in the graph.") from err
        for u in nbrs:
            del adj[u][n]
        del adj[n]

    def remove_nodes_from(self, nodes):
        adj = self._adj
        for n in nodes:
            try:
                del self._nodes[n]
                for u in list(adj[n]):  # list handles self-loops
                    del adj[u][n]  # (allows mutation of dict in loop)
                del adj[n]
            except KeyError:
                pass

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
            elif len_e == 3:
                u, v, attr = e
            else:
                raise Exception(f"Edge tuple {e} must be a 2-tuple or 3-tuple")

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

    def has_edge(self, u, v):
        try:
            return v in self._adj[u]
        except KeyError:
            return False

    def adjacency(self):
        return iter(self._adj.items())

    def is_multigraph(self):
        return False

    def number_of_nodes(self):
        return len(self._nodes)

    def number_of_edges(self):
        return len(self.edges)

    def copy(self):
        G = self.__class__(self._adj)
        return G
