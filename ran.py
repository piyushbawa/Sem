import networkx as nx
import numpy as np

def random_walk(G, start_node, steps):
    current_node = start_node
    for i in range(steps):
        neighbors = list(G.neighbors(current_node))
        if len(neighbors) == 0:
            return current_node
        else:
            current_node = np.random.choice(neighbors)
    return current_node

def hitting_time(G, start_node, target_node, num_samples=1000):
    total_time = 0
    for i in range(num_samples):
        current_node = start_node
        steps = 0
        while current_node != target_node:
            current_node = random_walk(G, current_node, 1)
            steps += 1
        total_time += steps
    return total_time / num_samples

def commute_time(G, start_node, target_node, num_samples=1000):
    ht_st_tg = hitting_time(G, start_node, target_node, num_samples)
    ht_tg_st = hitting_time(G, target_node, start_node, num_samples)
    return ht_st_tg + ht_tg_st
# Example social network
G = nx.karate_club_graph()
# Example usage
ht = hitting_time(G, 0, 33, num_samples=10000)
print("hitting",ht)
# Example usage
ct = commute_time(G, 0, 33, num_samples=10000)
print("commuting",ct)
