from graphs import bfs, dfs, ucs, greedy_bfs, a_star

# main.py

# Declare the graph as an adjacency list with edge weights
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('E',3),('D', 1)],
    'D': [('F', 2)],
    'E': [('F', 1)],
    'F': [('F',3)],
    'G': []  
}

# Declare the heuristic values for each node
heuristics = {
    'A': 7, 'B':6 , 'C':4, 'D':3, 'E':2, 'F':1, 'G':0
}
