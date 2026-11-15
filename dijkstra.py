
import json
import heapq


def dijkstra(graph, start):
    """
    Find shortest distances from a starting location
    to all other locations using Dijkstra's algorithm.
    """

    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (distance, neighbor)
                )

    return distances, previous


def get_path(previous, destination):

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path


def find_shortest_path(filename="data/locations.json"):

    with open(filename, "r") as file:
        data = json.load(file)

    graph = data["graph"]
    start = data["depot"]

    distances, previous = dijkstra(graph, start)

    print("\n===== DIJKSTRA SHORTEST PATHS =====")

    for destination in graph:

        if distances[destination] == float("inf"):
            print(f"{start} to {destination}: No path available")
            continue

        path = get_path(previous, destination)

        print(
            f"{start} to {destination}: "
            f"{' -> '.join(path)} | "
            f"Distance: {distances[destination]} km"
        )


if __name__ == "__main__":
    find_shortest_path()
