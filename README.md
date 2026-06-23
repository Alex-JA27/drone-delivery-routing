# Drone Delivery Routing

This project solves a drone delivery routing problem using Dijkstra’s algorithm.

The drone starts at a warehouse, delivers two packages to two destinations, and returns to the warehouse. The goal is to find the shortest possible round trip.

## Problem

Given:
- A weighted undirected graph
- A warehouse starting point
- Two delivery destinations
- Non-negative flight distances between locations

Find the shortest route:

Warehouse → Destination 1 → Destination 2 → Warehouse

or

Warehouse → Destination 2 → Destination 1 → Warehouse

The algorithm compares both possible delivery orders and returns the cheaper one.

## Algorithm Used

This project uses Dijkstra’s algorithm because all edge weights are non-negative.

Dijkstra is run twice:
1. From the warehouse
2. From the first destination

These shortest-path distances are used to compare the two possible delivery routes.

## Runtime

Using a binary min-heap, Dijkstra’s algorithm runs in:

O((N + M) log N)

Since the algorithm runs Dijkstra twice, the total runtime is still:

O((N + M) log N)

## Files

- `main.py` - Runs the drone delivery routing example
- `dijkstra.py` - Contains Dijkstra’s algorithm
- `graph.py` - Builds the graph
- `examples/sample_graph.txt` - Example input graph

## Example

```python
warehouse = "A"
destination1 = "C"
destination2 = "E"
