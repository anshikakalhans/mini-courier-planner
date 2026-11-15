
import json
from dijkstra import dijkstra, get_path
from knapsack import knapsack
from sorting import merge_sort


def nearest_neighbor_tsp(graph, start, destinations):
    """
    Generate an approximate delivery route using
    the Nearest Neighbor TSP algorithm.
    """

    # Remove duplicate destinations and depot
    unvisited = set(destinations)
    unvisited.discard(start)

    current = start
    route = [start]
    total_distance = 0

    while unvisited:

        # Find shortest distances from current location
        distances, _ = dijkstra(graph, current)

        # Select nearest unvisited destination
        next_location = min(
            unvisited,
            key=lambda node: distances[node]
        )

        total_distance += distances[next_location]

        route.append(next_location)
        unvisited.remove(next_location)
        current = next_location

    # Return to depot
    distances, _ = dijkstra(graph, current)

    total_distance += distances[start]
    route.append(start)

    return route, total_distance


def generate_delivery_route():

    with open("data/locations.json", "r") as file:
        location_data = json.load(file)

    with open("data/parcels.json", "r") as file:
        parcel_data = json.load(file)

    graph = location_data["graph"]
    depot = location_data["depot"]

    # Select parcels using Knapsack
    parcels = merge_sort(parcel_data["parcels"])

    selected, _ = knapsack(
        parcels,
        parcel_data["vehicle_capacity"]
    )

    # Get unique delivery destinations
    destinations = list(
        set(parcel["destination"] for parcel in selected)
    )

    route, distance = nearest_neighbor_tsp(
        graph,
        depot,
        destinations
    )

    print("\n===== NEAREST NEIGHBOR DELIVERY ROUTE =====")

    print("Selected Destinations:", destinations)

    print("Delivery Route:", " -> ".join(route))

    print("Total Route Distance:", distance, "km")

    print("\n===== ROAD PATH DETAILS =====")

    for i in range(len(route) - 1):

        distances, previous = dijkstra(graph, route[i])

        path = get_path(previous, route[i + 1])

        print(
            f"{route[i]} to {route[i + 1]}: "
            f"{' -> '.join(path)} | "
            f"{distances[route[i + 1]]} km"
        )


if __name__ == "__main__":
    generate_delivery_route()
