import typing

_edges = [
    ["W", "X"],
    ["X", "Y"],
    ["Y", "Z"],
    ["Z", "V"],
    ["V", "W"],
]


def build_graph(edges: typing.List[typing.AnyStr]):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


"""
W--X--Y-- Z
\        /
 V ----/
"""

from queue import Queue


def shortest_path(graph, start, dest) -> int:
    # using bfs
    visited = set()
    queue = Queue()
    queue.put([start, 0])

    while queue.empty() is False:
        curr = queue.get()
        curr_node, distance = curr

        if curr_node == dest:
            return distance

        visited.add(curr_node)

        for neighbor in graph[curr_node]:
            if neighbor not in visited:
                queue.put((neighbor, distance + 1))

    return -1


if __name__ == '__main__':
    print(shortest_path(build_graph(_edges), "W", "Z"))
