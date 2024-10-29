import heapq

# class for graph
class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, u, v, weight):
        if u not in self.nodes:
            self.nodes[u] = []
        if v not in self.nodes:
            self.nodes [v] = []

    # adding edges with weight
        self.nodes[u].append((v, weight))
        self.nodes[v].append((u, weight))

    def dijkstra(self, start):
        # starting distances are infinity
        distances = {node: float('infinity') for node in self.nodes}
        distances[start] = 0

        # bynary heap
        priority_queue = [(0,start)]
        heapq.heapify(priority_queue)

        # save shortest path
        shortest_paths = {start: None}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node]:
                continue
            # checking all neighbors of current node
            for neighbor, weight in self.nodes[current_node]:
                distance = current_distance + weight

                # if shortes way found -> update distance and add it to queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    shortest_paths[neighbor] = current_node

        return distances, shortest_paths
    
    # testing
if __name__ == "__main__":
    graph = Graph()

    # making graph
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)
    graph.add_edge('D', 'E', 3)

   
    # implementing dijkstra from A
    start_vertex = 'A'
    distances, shortest_paths = graph.dijkstra(start_vertex)

    # results
    print(f"Shortest path from {start_vertex}:")
    for node, distance in distances.items():
        print(f"Distance to {node}: {distance}")

    print("\nPaths for each node:")
    for node, predecessor in shortest_paths.items():
        if predecessor is None:
            print(f"Node {node} - predecessor{predecessor}")
        else:
            print(f"Node {node} - starting point")

