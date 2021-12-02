import networkx as nx
from algorithms.undirected import *
import numpy as np
from algorithms.build_cluster import *
from math import log
import matplotlib.pyplot as plt

# node 1 , node 6, node 10
# graph_edges = [(2, 1), (3, 1), (4, 1), (5, 1),
#                (7, 6), (8, 6), (9, 6),
#                (11, 10), (12, 10), (13, 10), (14, 10),
#                (2, 9), (8, 11), (3, 14), (4, 13)]
#
# G = nx.Graph(graph_edges)
# g = G.adj

# import time
# st = time.time()
# print('Shortest Path: ', dict(shortest_path(g, 1)))
# print('Distance between: ', get_distance_between(g, 1, 10))
# print('Vertices in distance: ', get_vertices_in_distance(g, 1, 3))
# print('Edges in distance: ', list(get_edges_in_distance(g, 1, 3)))
# print('Diameter of Graph: ', get_diameter(g))
# print('all Pairs Path: ', dict(all_paris_shortest_path(g)))
# print(time.time()-st)
#
# # graph_edges
# print(len(graph_edges))

# get_diameter(G)
#
# d = 15
# C = len(graph_edges)
# a = 4*log(C)/d
# print(a)
# # k = build_cluster(g,1,a)
# # print(a)
# build_partition(G, 1, 1)
#
# print(G.edges)

graph_edges = [(2, 1), (3, 1), (4, 1), (5, 1),
               (7, 6), (8, 6), (9, 6),
               (11, 10), (12, 10), (13, 10), (14, 10),
               (2, 9), (8, 11), (3, 14), (4, 13)]

G = nx.Graph(graph_edges)
print(G.number_of_nodes())

root = [1, 6, 10]
a = {1: [2, 3, 4, 5], 6: {7, 8, 9}, 10: {11, 12, 13, 14}}
for r in root:
    for u in a[r]:
        G = nx.contracted_nodes(G, r, u, self_loops=True)

print(G.adj)
# print(G.number_of_nodes())
print(G.adj[1])

# nx.draw(G)
# plt.draw()
# plt.savefig('b.jpg')
