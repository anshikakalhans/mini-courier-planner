
import time
import random
import csv
import os
import matplotlib.pyplot as plt

from sorting import merge_sort
from knapsack import knapsack
from dijkstra import dijkstra
from tsp import nearest_neighbor_tsp


def generate_parcels(n, locations, rng):
    """Generate sample parcels for performance testing."""

    parcels = []

    for i in range(n):
        parcels.append({
            "id": f"P{i + 1}",
            "destination": rng.choice(locations[1:]),
            "weight": rng.randint(1, 10),
            "priority": rng.randint(1, 5),
            "priority_score": rng.randint(10, 100),
            "deadline": "12:00"
        })

    return parcels


def generate_graph(n, rng):
    """Generate a connected, undirected road graph."""

    locations = ["A"] + [f"L{i}" for i in range(1, n + 1)]

    graph = {node: {} for node in locations}

    # Connect locations in a ring to ensure connectivity
    for i in range(len(locations)):
        u = locations[i]
        v = locations[(i + 1) % len(locations)]

        weight = rng.randint(1, 20)

        graph[u][v] = weight
        graph[v][u] = weight

    # Add additional random roads
    for i in range(len(locations)):
        for j in range(i + 2, len(locations)):

            if i == 0 and j == len(locations) - 1:
                continue

            if rng.random() < 0.12:

                u = locations[i]
                v = locations[j]

                weight = rng.randint(1, 20)

                graph[u][v] = weight
                graph[v][u] = weight

    return graph, locations


def measure_runtime(function, repeats=3):
    """Calculate average execution time in milliseconds."""

    total_time = 0

    for _ in range(repeats):

        start = time.perf_counter()

        function()

        end = time.perf_counter()

        total_time += end - start

    return (total_time / repeats) * 1000


def run_performance_tests():

    print("\n===== PERFORMANCE TESTING =====")

    sizes = [10, 20, 40, 80, 120]

    results = []

    for n in sizes:

        rng = random.Random(42 + n)

        parcels = generate_parcels(n, ["A"] + [
            f"L{i}" for i in range(1, n + 1)
        ], rng)

        graph, locations = generate_graph(n, rng)

        capacity = max(
            10,
            int(sum(p["weight"] for p in parcels) * 0.35)
        )

        # Prepare sorted parcels for Knapsack
        sorted_parcels = merge_sort(parcels)

        # Prepare selected destinations for TSP
        selected, _ = knapsack(sorted_parcels, capacity)

        destinations = sorted(set(
            p["destination"] for p in selected
        ))

        # Measure each algorithm
        sorting_time = measure_runtime(
            lambda: merge_sort(parcels)
        )

        knapsack_time = measure_runtime(
            lambda: knapsack(sorted_parcels, capacity)
        )

        dijkstra_time = measure_runtime(
            lambda: dijkstra(graph, "A")
        )

        tsp_time = measure_runtime(
            lambda: nearest_neighbor_tsp(
                graph, "A", destinations
            )
        )

        results.append({
            "Input Size": n,
            "Sorting (ms)": sorting_time,
            "Knapsack (ms)": knapsack_time,
            "Dijkstra (ms)": dijkstra_time,
            "TSP (ms)": tsp_time
        })

        print(f"\nInput Size: {n}")

        print(f"Sorting: {sorting_time:.4f} ms")
        print(f"Knapsack: {knapsack_time:.4f} ms")
        print(f"Dijkstra: {dijkstra_time:.4f} ms")
        print(f"TSP: {tsp_time:.4f} ms")

    # Create results directory
    os.makedirs("results", exist_ok=True)

    # Save runtime results in CSV
    with open("results/runtime_results.csv", "w",
              newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=results[0].keys()
        )

        writer.writeheader()
        writer.writerows(results)

    # Generate runtime comparison chart
    sizes = [row["Input Size"] for row in results]

    plt.figure(figsize=(10, 6))

    for column in [
        "Sorting (ms)",
        "Knapsack (ms)",
        "Dijkstra (ms)",
        "TSP (ms)"
    ]:

        values = [row[column] for row in results]

        plt.plot(
            sizes,
            values,
            marker="o",
            label=column
        )

    plt.xlabel("Input Size")
    plt.ylabel("Average Execution Time (ms)")
    plt.title("Mini-Courier Planner - Runtime Comparison")

    plt.yscale("log")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("results/runtime_comparison.png")

    plt.show()

    print("\n===== PERFORMANCE TESTING COMPLETED =====")
    print("CSV saved: results/runtime_results.csv")
    print("Chart saved: results/runtime_comparison.png")


if __name__ == "__main__":
    run_performance_tests()
