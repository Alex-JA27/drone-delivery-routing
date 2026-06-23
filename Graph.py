
---

## graph.py

```python
def build_graph(edges):
    graph = {}

    for u, v, weight in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append((v, weight))
        graph[v].append((u, weight))

    return graph
