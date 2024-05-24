import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dejkstri_search(graph, start):
    '''Алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі'''
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

def visualize_graph(graph):
    '''Візуалізація графа'''
    G = nx.Graph()
    for node in graph:
        G.add_node(node)
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)  # Розташування вершин
    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Граф")
    plt.show()

# Приклад використання:
graph = {
    'A': {'B': 13, 'C': 14},
    'B': {'A': 13, 'C': 2, 'D': 5},
    'C': {'A': 14, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

visualize_graph(graph)

start_vertex = 'A'
shortest_distances = dejkstri_search(graph, start_vertex)
print("Найкоротші відстані від вершини", start_vertex)
for vertex, distance in shortest_distances.items():
    if vertex == start_vertex:
        continue
    print(f"{start_vertex} -> {vertex}: відстань {distance}")
