from collections import deque
import networkx as nx
from task_1 import G

# DFS реалізація
def dfs(graph, start, path=[]):
    path.append(start)
    for neighbor in graph[start]:
        if neighbor not in path:
            dfs(graph, neighbor, path)
    return path

# BFS реалізація
def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

# Перетворимо graph у формат adjacency list для алгоритмів
graph_dict = nx.to_dict_of_lists(G)

print("DFS:", dfs(graph_dict, "Pokrovska"))
print("BFS:", bfs(graph_dict, "Pokrovska"))
