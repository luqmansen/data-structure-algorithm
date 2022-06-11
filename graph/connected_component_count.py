"""
1 -- 2
|
3 -- 4

5 -- 6

7 -- 8

there should be 3 component
"""
import typing

_graph = {
    1: [2, 3],
    2: [1],
    3: [1, 4],
    4: [3],
    5: [6],
    6: [5],
    7: [8],
    8: [7]
}


def count_connected_component(graph: typing.Dict[int, typing.List[int]]):
    count = 0
    visited = set()
    for node, _ in graph.items():
        if explore_node_recursive(graph, node, visited):
            count += 1

    print(count)


def explore_node(graph, node, visited: typing.Set) -> bool:
    # dfs search
    if node in visited:
        return False

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
    return len_before != len(visited)


"""
1 -- 2
|
3 -- 4

5 -- 6

7 -- 8
"""


def explore_node_recursive(graph, node, visited: typing.Set) -> bool:
    # dfs search
    if node in visited:
        return False

    visited.add(node)

    for neighbor in graph[node]:
        explore_node_recursive(graph, neighbor, visited)

    return True


if __name__ == '__main__':
    count_connected_component(_graph)
