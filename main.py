
import json

from sorting import merge_sort
from knapsack import knapsack
from dijkstra import dijkstra, get_path
from tsp import nearest_neighbor_tsp


def main():

    # Load datasets
    with open("data/parcels.json", "r") as file:
        parcel_data = json.load(file)

    with open("data/locations.json", "r") as file:
        location_data = json.load(file)

    parcels = parcel_data["parcels"]
    capacity = parcel_data["vehicle_capacity"]
    graph = location_data["graph"]
    depot = location_data["depot"]

    print("\n======================================")
    print("       MINI-COURIER PLANNER")
    print("======================================")

    # STEP 1: Sort parcels
    print("\n1. PARCEL PRIORITIZATION")

    sorted_parcels = merge_sort(parcels)

    for parcel in sorted_parcels:
        print(
            f'{parcel["id"]} | '
            f'Priority: {parcel["priority_score"]} | '
            f'Deadline: {parcel["deadline"]}'
        )

    # STEP 2: Optimize packing
    print("\n2. OPTIMIZED PACKING PLAN")

    selected, max_score = knapsack(
        sorted_parcels,
        capacity
    )

    total_weight = sum(
        parcel["weight"] for parcel in selected
    )

    for parcel in selected:
        print(
            f'{parcel["id"]} | '
            f'{parcel["weight"]} kg | '
            f'Score: {parcel["priority_score"]}'
        )

    print("Vehicle Capacity:", capacity, "kg")
    print("Total Weight:", total_weight, "kg")
    print("Remaining Capacity:", capacity - total_weight, "kg")
    print("Maximum Priority Score:", max_score)

    # STEP 3: Find shortest paths using Dijkstra
    print("\n3. DIJKSTRA SHORTEST PATHS")

    distances, previous = dijkstra(graph, depot)

    for destination in graph:

        if distances[destination] == float("inf"):
            print(f"{depot} to {destination}: No path available")
            continue

        path = get_path(previous, destination)

        print(
            f'{depot} to {destination}: '
            f'{" -> ".join(path)} | '
            f'{distances[destination]} km'
        )

    # STEP 4: Generate delivery route using TSP
    print("\n4. OPTIMIZED DELIVERY ROUTE")

    destinations = sorted(set(
        parcel["destination"] for parcel in selected
    ))

    route, total_distance = nearest_neighbor_tsp(
        graph,
        depot,
        destinations
    )

    print("Delivery Destinations:", destinations)
    print("Delivery Route:", " -> ".join(route))
    print("Total Route Distance:", total_distance, "km")

    print("\n======================================")
    print("       COURIER PLAN COMPLETED")
    print("======================================")


if __name__ == "__main__":
    main()
