from collections import Mapping


class AtlasView(Mapping):

    __slots__ = ("_atlas",)

    def __getstate__(self):
        return {"_atlas": self._atlas}

    def __setstate__(self, state):
        self._atlas = state["_atlas"]

    def __init__(self, d):
        self._atlas = d

    def __len__(self):
        return len(self._atlas)

    def __iter__(self):
        return iter(self._atlas)

    def __getitem__(self, key):
        return self._atlas[key]

    def copy(self):
        return {n: self[n].copy() for n in self._atlas}

    def __str__(self):
        return str(self._atlas)  # {nbr: self[nbr] for nbr in self})

    def __repr__(self):
        return f"{self.__class__.__name__}({self._atlas!r})"


class AdjacencyView(AtlasView):
    __slots__ = ()  # Still uses AtlasView slots names _atlas

    def __getitem__(self, name):
        return AtlasView(self._atlas[name])

    def copy(self):
        return {n: self[n].copy() for n in self._atlas}


class EdgeView:
    def __init__(self, G):
        self._adjdict = G._adj
        self._nodes_nbrs = self._adjdict.items

    def __iter__(self):
        for n, nbrs in self._nodes_nbrs():
            for nbr in nbrs:
                yield (n, nbr)

    def __contains__(self, e):
        try:
            u, v = e
            return v in self._adjdict[u]
        except KeyError:
            return False

    def __getitem__(self, e):
        if isinstance(e, slice):
            raise "Error"
        u, v = e
        return self._adjdict[u][v]

    def __call__(self, nbunch=None, data=False, default=None):
        if nbunch is None and data is False:
            return self
        return "Callable EgeView"

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({list(self)})"
