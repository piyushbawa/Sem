import networkx as nx

# Example social network
G = nx.karate_club_graph()
print(G)
# Compute centrality measures
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

# Compute proximity prestige measures
eccentricity = nx.eccentricity(G)
harmonic_centrality = nx.harmonic_centrality(G)

# Print the results
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
