from pprint import pprint
from typing import List, Dict, Union

_edges = [
    ["i", "j"],
    ["j", "k"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]


def convert_edge_to_adj_list(edges: List[str]) -> Dict[str, Union[List[str], List]]:
    adj_list = {}
    for edge in edges:
        a, b = edge
        if a not in adj_list:
            adj_list[a] = []
        if b not in adj_list:
            adj_list[b] = []

        adj_list[a].append(b)
        adj_list[b].append(a)

    return adj_list


def undirected_path(
        edges: List[str],
        src, dst: str
) -> bool:
    if src == dst:
        return True

    graph = convert_edge_to_adj_list(edges)
    visited = set()
    stack = [src]

    while len(stack) > 0:
        curr = stack.pop()
        if curr == dst:
            return True

        visited.add(curr)

        for i in graph[curr]:
            if i not in visited:
                stack.append(i)

    return False


"""
i -- j
|
k -- L
|
m

o -- n
"""

if __name__ == '__main__':
    print(undirected_path(_edges, "i", "m"))
    print(undirected_path(_edges, "i", "o"))
