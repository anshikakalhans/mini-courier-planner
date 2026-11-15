
import json
from sorting import merge_sort


def knapsack(parcels, capacity):
    """
    Select parcels using 0/1 Knapsack Dynamic Programming.
    Maximize priority score within vehicle capacity.
    """

    n = len(parcels)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):

        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["priority_score"]

        for w in range(capacity + 1):

            if weight <= w:

                dp[i][w] = max(
                    value + dp[i - 1][w - weight],
                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected parcels
    selected = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected.append(parcels[i - 1])
            w -= parcels[i - 1]["weight"]

    selected.reverse()

    return selected, dp[n][capacity]


def optimize_packing(filename="data/parcels.json"):

    with open(filename, "r") as file:
        data = json.load(file)

    parcels = merge_sort(data["parcels"])
    capacity = data["vehicle_capacity"]

    selected, max_score = knapsack(parcels, capacity)

    total_weight = sum(p["weight"] for p in selected)

    print("\n===== OPTIMIZED PACKING PLAN =====")

    for parcel in selected:
        print(
            f'{parcel["id"]} | '
            f'Weight: {parcel["weight"]} kg | '
            f'Priority Score: {parcel["priority_score"]}'
        )

    print("\nVehicle Capacity:", capacity, "kg")
    print("Total Weight:", total_weight, "kg")
    print("Remaining Capacity:", capacity - total_weight, "kg")
    print("Maximum Priority Score:", max_score)


if __name__ == "__main__":
    optimize_packing()
