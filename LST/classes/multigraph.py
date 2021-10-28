from .graph import Graph

__all__ = ["MultiGraph"]


class MultiGraph(Graph):
    edge_key_dict_factory = dict

    def __init__(self, egdes_data=None):
        self.edge_key_dict_factory = self.edge_key_dict_factory
        Graph.__init__(self, egdes_data)

    def new_edge_key(self, u, v):
        try:
            keydict = self._adj[u][v]
        except:
            return 0
        key = len(keydict)
        while key in keydict:
            key += 1
        return key

    def add_edge(self, edge_u, edge_v, key=None, **attr):
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

        if key is None:
            key = self.new_edge_key(u, v)
        if v in self._adj[u]:
            keydict = self._adj[u][v]
            datadict = keydict.get(key, self.edge_attr_dict_factory())
            datadict.update(attr)
            keydict[key] = datadict
        else:
            datadict = self.edge_attr_dict_factory()
            datadict.update(attr)
            keydict = self.edge_key_dict_factory()
            keydict[key] = datadict
            self._adj[u][v] = keydict
            self._adj[v][u] = keydict
        return key

    def is_multigraph(self):
        return True

