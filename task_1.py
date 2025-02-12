import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = [
    "Parus",
    "Pokrovska",
    "Prospekt Svobody",
    "Zavodska",
    "Metalurgiv",
    "Metrobudivnykiv",
    "Vokzalna",
    "Zaliznychnyy vokzal",
    "Teatralna",
    "Centralna",
    "Muzejna",
    "Dnipro",
]
G.add_nodes_from(stations)

connections_active = [
    ("Pokrovska", "Prospekt Svobody"),
    ("Prospekt Svobody", "Zavodska"),
    ("Zavodska", "Metalurgiv"),
    ("Metalurgiv", "Metrobudivnykiv"),
    ("Metrobudivnykiv", "Vokzalna"),
    ("Vokzalna", "Zaliznychnyy vokzal"),
]
connections_inactive = [
    ("Parus", "Pokrovska"),
    ("Vokzalna", "Teatralna"),
    ("Teatralna", "Centralna"),
    ("Centralna", "Muzejna"),
    ("Muzejna", "Dnipro"),
]
G.add_edges_from(connections_active + connections_inactive)

plt.figure(figsize=(8, 6))

pos = nx.spring_layout(G)

nx.draw_networkx_edges(
    G, pos, edgelist=connections_active, edge_color='red', width=2, style='solid'
)

nx.draw_networkx_edges(
    G, pos, edgelist=connections_inactive, edge_color='gray', width=2, style='dashed'
)

nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=2000)

nx.draw_networkx_labels(G, pos, font_size=15, font_weight='bold')

plt.title("Metro Stations in Dnipro", fontsize=16)
plt.show()

print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин:", dict(G.degree()))
