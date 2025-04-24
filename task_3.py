graph = {
    "Pokrovska": {"Prospekt Svobody": 1000, "Parus": 1800},
    "Prospekt Svobody": {"Pokrovska": 1000, "Zavodska": 1300},
    "Zavodska": {"Prospekt Svobody": 1300, "Metalurgiv": 1100},
    "Metalurgiv": {"Zavodska": 1100, "Metrobudivnykiv": 900},
    "Metrobudivnykiv": {"Metalurgiv": 900, "Vokzalna": 1200},
    "Vokzalna": {"Metrobudivnykiv": 1200, "Zaliznychnyy vokzal": 300, "Teatralna": 900},
    "Zaliznychnyy vokzal": {"Vokzalna": 300},
    "Parus": {"Pokrovska": 1800},
    "Teatralna": {"Vokzalna": 900, "Centralna": 600},
    "Centralna": {"Teatralna": 600, "Muzejna": 700},
    "Muzejna": {"Centralna": 700, "Dnipro": 800},
    "Dnipro": {"Muzejna": 800}
}

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

    return distances

print("Найкоротші шляхи між усіма вершинами (в метрах):\n")

for start in graph.keys():
    distances = dijkstra(graph, start)
    for end, dist in distances.items():
        print(f"Від {start} до {end}: {dist} м")
    print("-" * 40)
