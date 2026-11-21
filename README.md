# Mini-Courier-Planner

## Project Overview

Mini-Courier Planner is a Python-based courier planning system that simulates an intelligent parcel delivery process.

The system prioritizes parcels, selects the optimal combination of parcels within vehicle capacity, calculates shortest paths between delivery locations, generates an approximate delivery route, and compares the execution time of different algorithms.

The project demonstrates the practical implementation of Design and Analysis of Algorithms concepts.

## Technologies Used

- Python 3
- JSON
- Matplotlib
- CSV
- Visual Studio Code

## Algorithms Implemented

### 1. Merge Sort

Used to sort parcels based on their priority scores in descending order.

- Time Complexity: O(n log n)

### 2. 0/1 Knapsack using Dynamic Programming

Used to select the optimal combination of parcels within the vehicle's maximum weight capacity while maximizing the total priority score.

- Time Complexity: O(n × W)
- Space Complexity: O(n × W)

### 3. Dijkstra's Shortest Path Algorithm

Used to calculate the shortest paths between delivery locations using a weighted graph and priority queue.

- Time Complexity: O((V + E) log V)

### 4. Nearest Neighbor TSP

Used to generate an approximate delivery route by visiting the nearest unvisited delivery location and returning to the starting depot.

- Uses Dijkstra's algorithm to calculate distances between locations.
- Produces an approximate route rather than guaranteeing the globally optimal TSP solution.

## Project Structure

```text
mini courier planner/
│
├── .gitignore
├── README.md
│
├── main.py
├── sorting.py
├── knapsack.py
├── dijkstra.py
├── tsp.py
├── performance.py
│
├── data/
│   ├── locations.json
│   └── parcels.json
│
├── results/
│   ├── runtime_comparison.png
│   └── runtime_results.csv
│
└── screenshots/
    ├── complete main.py output.png
    ├── dijkstra output.png
    ├── folder structure.png
    ├── knapsack brute force verification.png
    ├── knapsack output.png
    ├── runtime comparison graph.png
    ├── runtime CSV results.png
    ├── sorting output.png
    └── tsp output.png
```

## Sample Dataset

The project uses JSON files to store parcel information and delivery locations.

- Total Parcels: 6
- Vehicle Capacity: 15 kg
- Delivery Locations: A, B, C, D, E
- Starting Depot: A

## Sample Results

The system produces the following results using the sample dataset:

| Parameter | Result |
|---|---|
| Total Parcels | 6 |
| Selected Parcels | 4 |
| Vehicle Capacity | 15 kg |
| Total Selected Weight | 15 kg |
| Maximum Priority Score | 290 |
| Brute-Force Verified Optimal Score | 290 |
| Delivery Route | A → B → C → D → A |
| Total Route Distance | 18 km |

## Installation and Execution

### Prerequisites

- Python 3 installed
- Visual Studio Code or another Python IDE

### Install Required Library

Open the terminal and execute:

```bash
python -m pip install matplotlib
```

### Run the Complete Application

```bash
python main.py
```

### Run Individual Algorithms

```bash
python sorting.py
python knapsack.py
python dijkstra.py
python tsp.py
```

### Run Performance Testing

```bash
python performance.py
```

## Performance Testing

The system evaluates algorithm performance using five different input sizes:

- 10
- 20
- 40
- 80
- 120

Each algorithm is executed multiple times, and the average execution time is calculated.

The performance results are stored in:

- `results/runtime_results.csv`
- `results/runtime_comparison.png`

## Screenshots

The `screenshots` folder contains the execution outputs of individual algorithms, the complete application, project structure, Knapsack brute-force verification, and runtime performance analysis.

## Conclusion

The Mini-Courier Planner successfully integrates sorting, dynamic programming, graph algorithms, and approximation techniques into a single courier planning application.

It demonstrates how algorithmic concepts can be applied to real-world problems involving parcel prioritization, vehicle capacity optimization, shortest path calculation, and delivery route planning.
