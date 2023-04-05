import networkx as nx
import numpy as np

adj_matrix = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])

G = nx.Graph()

n = len(adj_matrix)
G.add_nodes_from(range(n))

for i in range(n):
    for j in range(i+1, n):
        if adj_matrix[i][j] == 1:
            G.add_edge(i,j)

# G = nx.karate_club_graph()
print(G)

degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

eccentricity = nx.eccentricity(G)
harmonic_centrality = nx.harmonic_centrality(G)

print("Degree Centrality:")
for node, centrality in degree_centrality.items():
    print(f"Node {node}: {centrality:.3f}")
print()

print("Closeness Centrality:")
for node, centrality in closeness_centrality.items():
    print(f"Node {node}: {centrality:.3f}")
print()

print("Betweenness Centrality:")
for node, centrality in betweenness_centrality.items():
    print(f"Node {node}: {centrality:.3f}")
print()

print("Eccentricity:")
for node, ecc in eccentricity.items():
    print(f"Node {node}: {ecc}")
print()

print("Harmonic Centrality:")
for node, centrality in harmonic_centrality.items():
    print(f"Node {node}: {centrality:.3f}")
