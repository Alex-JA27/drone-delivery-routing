from graph import build_graph
from dijkstra import dijkstra, get_path


def deliver_two_packages(graph, warehouse, d1, d2):
    dist_from_warehouse, prev_from_warehouse = dijkstra(graph, warehouse)
    dist_from_d1, prev_from_d1 = dijkstra(graph, d1)

    cost_a = (
        dist_from_warehouse[d1]
        + dist_from_d1[d2]
        + dist_from_warehouse[d2]
    )

    cost_b = (
        dist_from_warehouse[d2]
        + dist_from_d1[d2]
        + dist_from_warehouse[d1]
    )

    if cost_a <= cost_b:
        first = d1
        second = d2
        total_cost = cost_a
    else:
        first = d2
        second = d1
        total_cost = cost_b

    leg1 = get_path(prev_from_warehouse, warehouse, first)

    if first == d1:
        leg2 = get_path(prev_from_d1, d1, d2)
    else:
        leg2 = get_path(prev_from_d1, d1, d2)
        leg2.reverse()

    leg3 = get_path(prev_from_warehouse, warehouse, second)
    leg3.reverse()

    route = leg1 + leg2[1:] + leg3[1:]

    return route, total_cost


def main():
    edges = [
        ("A", "B", 2),
        ("A", "C", 5),
        ("B", "C", 1),
        ("B", "D", 4),
        ("C", "D", 2),
        ("C", "E", 6),
        ("D", "E", 1),
    ]

    graph = build_graph(edges)

    warehouse = "A"
    destination1 = "C"
    destination2 = "E"

    route, distance = deliver_two_packages(
        graph,
        warehouse,
        destination1,
        destination2
    )

    print("Best route:", " -> ".join(route))
    print("Total distance:", distance)


if __name__ == "__main__":
    main()
