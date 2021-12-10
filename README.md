# Low-stretch-trees

## LST 
LST is a Python package for the creation, manipulation, and study of the low-stretch tree.<br>

###Install 
``$ git clone https://github.com/travis0120/Low-stretch-trees.git``
<br>
``$ cd Low-stretch-trees``
<br>

##Tutorial 

###Create a Graph 
``>> import LST as lst``<br>
``>> G = lst.Graph()``<br>

### Add a Node 
``>> import LST as lst``<br>
``>> G = lst.Graph()``<br>
``>> G.add_node("node_1")``<br>
``>> G.add_node("node_2")``<br>
``>> G.add_node(3)``
``>> G.nodes``<br>
``{'node_1': {}, 'node_2': {}, 3: {}}``<br>
or<br>
``>> G.add_nodes_from(["node_1", "node_2", 3])``<br>
``>> G.nodes``<br>
``{'node_1': {}, 'node_2': {}, 3: {}}``<br>

### Remove a Node
``>> G.nodes``<br>
``{'node_1': {}, 'node_2': {}, 3: {}}``<br>
``>> G.remove_node("node_2")``<br>
``{'node_1': {}, 3: {}}``<br>
or<br>
``>> G.remove_nodes_from(["node_2", 3])``<br>
``{'node_1': {}}``<br>

### Add a Edges
``>> import LST as lst``<br>
``>> G = lst.Graph()``<br>
``>> G.add_edge("node_1", 2)``<br>
``>> G.nodes``<br>
``{'node_1': {}, 2: {}}``<br>
``>> G.edges``<br>
``EdgeView([('node_1', 2)])``
or<br>
``>> G.add_edges_from([[(1, 2), (2,3), ... (node_u, node_v)]])``

### View Graph Adjacency
``>> G = lst.Graph()``<br>
``>> G.add_edge("node_1", 2)``<br>
``>> G.adj``<br>
``AdjacencyView({'node_1': {2: {}}, 2: {'node_1': {}}})``

### Get a Low-stretch Tree
``>> G = lst.Graph()``<br>
``>> G.add_edges_from([(1, 2), (2,3), ... (node_u, node_v)])``<br>
``>> T = lst.low_stretch_tree(G)``

### Get a Randomly weight minimum spanning tree
``>> G = lst.Graph()``<br>
``>> G.add_edges_from([(1, 2), (2,3), ... (node_u, node_v)])``<br>
``>> T = lst.random_mst(G)``