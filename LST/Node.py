import random
import LST as lst

graph_edges = [(2, 1), (3, 1), (4, 1), (5, 1),
               (7, 6), (8, 6), (9, 6),
               (11, 10), (12, 10), (13, 10), (14, 10),
               (2, 9), (8, 11), (3, 14), (4, 13)]

G = lst.Graph()
choices = [(2, 25), (27, 50), (52, 75), (77, 100)]

for i in range(2, 26):
    G.add_edge(1, i)

for i in range(27, 51):
    G.add_edge(26, i)

for i in range(52, 76):
    G.add_edge(51, i)

for i in range(77, 100):
    G.add_edge(76, i)

for i in range(10):
    a, b = random.randint(0, 3), random.randint(0, 3)
    c1, c2 = choices[a], choices[b]
    v1, v2 = random.randint(*c1), random.randint(*c2)
    G.add_edge(v1, v2)

T = lst.low_stretch_tree(G)
print(T.adj)
