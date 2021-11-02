import networkx as nx
from algorithms.undirected import *
import numpy as np


graph_edges = [(2, 1), (3, 1), (4, 1), (5, 1),
               (7, 6), (8, 6), (9, 6),
               (11, 10), (12, 10), (13, 10), (14, 10),
               (2, 9), (8, 11), (3, 14), (4, 13)]

G = nx.Graph(graph_edges)
g = G.adj

print('Shortest Path: ', dict(shortest_path(g, 1)))
print('Distance between: ', get_distance_between(g, 1, 10))
print('Vertices in distance: ', get_vertices_in_distance(g, 1, 3))
print('Edges in distance: ', list(get_edges_in_distance(g, 1, 3)))
print('Diameter of Graph: ', get_diameter(g))
print('all Pairs Path: ', dict(all_paris_shortest_path(g)))
