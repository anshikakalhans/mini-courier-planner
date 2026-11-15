
import json


def merge_sort(parcels):
    """
    Sort parcels by priority score in descending order.
    Uses Merge Sort algorithm.
    """

    if len(parcels) <= 1:
        return parcels

    mid = len(parcels) // 2

    left = merge_sort(parcels[:mid])
    right = merge_sort(parcels[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i]["priority_score"] >= right[j]["priority_score"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def prioritize_parcels(filename="data/parcels.json"):

    with open(filename, "r") as file:
        data = json.load(file)

    parcels = data["parcels"]

    sorted_parcels = merge_sort(parcels)

    print("\n===== PRIORITIZED PARCELS =====")

    for parcel in sorted_parcels:
        print(
            f'{parcel["id"]} | '
            f'Priority Score: {parcel["priority_score"]} | '
            f'Deadline: {parcel["deadline"]}'
        )

    return sorted_parcels


if __name__ == "__main__":
    prioritize_parcels()
