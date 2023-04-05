import numpy as np

def page_rank(adjacency_matrix, damping_factor=0.85, convergence_threshold=0.0001):
    # Create the transition probability matrix
    row_sum = np.sum(adjacency_matrix, axis=1)
    transition_matrix = adjacency_matrix / row_sum[:, np.newaxis]
    
    # Initialize the PageRank vector
    n = adjacency_matrix.shape[0]
    page_rank_vector = np.ones(n) / n
    
    # Perform the PageRank iterations
    while True:
        new_page_rank_vector = ((1 - damping_factor) / n) + (damping_factor * transition_matrix.T @ page_rank_vector)
        if np.max(np.abs(new_page_rank_vector - page_rank_vector)) < convergence_threshold:
            break
        page_rank_vector = new_page_rank_vector
    
    return page_rank_vector
# Example adjacency matrix
adjacency_matrix = np.array([[0, 0, 1, 0],
                             [1, 0, 0, 0],
                             [0, 1, 0, 1],
                             [0, 1, 0, 0]])
# Example usage
page_rank_vector = page_rank(adjacency_matrix, damping_factor=0.85, convergence_threshold=0.0001)
print(page_rank_vector)
