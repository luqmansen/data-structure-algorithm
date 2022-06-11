import typing

"""
   5
   | \ 
1--0--8

4--2
| /
3
"""

_graph = {
    0: [1, 5, 8],
    1: [0],
    2: [4, 3],
    3: [2, 4],
    4: [2, 3],
    5: [0, 8],
    8: [0, 5]
}


def count_largest_component(graph: typing.Dict[int, typing.List[int]]):
    visited = set()
    largest = 0
    for node, _ in graph.items():
        new_island, cnt = explore_node(graph, node, visited)
        if new_island:
            largest = max(largest, cnt)

    print(largest)


def explore_node(graph, node, visited: typing.Set) -> (bool, int):
    # dfs search
    if node in visited:
        return False, 0

    len_before = len(visited)

    stack = [node]
    while len(stack) > 0:
        curr = stack.pop()
        visited.add(curr)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                stack.append(neighbor)

    # if the number of visited node is increase after explore operation,
    # means that those nodes aren't connected to prev graph
    len_after = len(visited)
    return len_before != len_after, len_after - len_before


"""
   5
   | \ 
1--0--8

4--2
| /
3
"""


def explore_node_recursive(graph, node, visited: typing.Set) -> (int):
    if node in visited:
        return 0

    visited.add(node)
    size = 1

    for neighbor in graph[node]:
        size += explore_node_recursive(graph, neighbor, visited)

    return size


def count_largest_component_recursive(graph: typing.Dict[int, typing.List[int]]):
    visited = set()
    largest = 0
    for node, _ in graph.items():
        largest = max(largest, explore_node_recursive(graph, node, visited))

    print(largest)


if __name__ == '__main__':
    count_largest_component(_graph)
    count_largest_component_recursive(_graph)
