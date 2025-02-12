import networkx as nx
import matplotlib.pyplot as plt

# Додаємо ваги до графа
weighted_connections = [
    ("Pokrovska", "Prospekt Svobody", 1000),
    ("Prospekt Svobody", "Zavodska", 1300),
    ("Zavodska", "Metalurgiv", 1100),
    ("Metalurgiv", "Metrobudivnykiv", 900),
    ("Metrobudivnykiv", "Vokzalna", 1200),
    ("Vokzalna", "Zaliznychnyy vokzal", 300),
    ("Parus", "Pokrovska", 1800),
    ("Vokzalna", "Teatralna", 900),
    ("Teatralna", "Centralna", 600),
    ("Centralna", "Muzejna", 700),
    ("Muzejna", "Dnipro", 800),
]

G = nx.Graph()
G.add_weighted_edges_from(weighted_connections)

# Додаємо ребра з вагами
for u, v, weight in weighted_connections:
    G.add_edge(u, v, weight=weight)

# Використання алгоритму Дейкстри для знаходження найкоротших шляхів
shortest_paths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))

# Виведення найкоротших шляхів між усіма вершинами
print("Найкоротші шляхи між усіма вершинами (в метрах):")
for source, paths in shortest_paths.items():
    for target, distance in paths.items():
        print(f"Від {source} до {target}: {distance} м")

# Візуалізація графа
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)

# Рисуємо активні рёбра
nx.draw_networkx_edges(G, pos, edgelist=weighted_connections, edge_color='red', width=2)

# Рисуємо узлы
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=2000)

# Додаємо підписи узлів
nx.draw_networkx_labels(G, pos, font_size=15, font_weight='bold')

# Додаємо підписи вагів рёбер
edge_labels = {(u, v): f"{w} м" for u, v, w in weighted_connections}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

plt.title("Dnipro Metro Graph with Weights", fontsize=16)
plt.show()