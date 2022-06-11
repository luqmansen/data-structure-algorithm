from typing import Dict, List, AnyStr, Union

# A --> C
# |     |
# v     v
# B     E
# |
# v
# D --> F
graph_input = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def depth_first_print_iter(
        graph: Dict[str, Union[List[AnyStr], List]],
        node_start: AnyStr
):
    stack = [node_start]

    while len(stack) > 0:
        curr = stack.pop()
        print(curr)

        for i in graph[curr]:
            stack.append(i)


def depth_first_print_recursive(graph: Dict[str, Union[List[AnyStr], List]], node_start: AnyStr):
    print(node_start)
    for i in graph[node_start]:
        depth_first_print_recursive(graph, i)


def breath_first_print(graph: Dict[str, Union[List[AnyStr], List]], node_start: AnyStr):
    q = [node_start]

    while len(q) > 0:
        curr = q.pop()
        print(curr)

        for i in graph[curr]:
            q.insert(0, i)


if __name__ == '__main__':
    # depth_first_print_iter(graph_input, "a")
    # depth_first_print_recursive(graph_input, "a")
    breath_first_print(graph_input, "a")
