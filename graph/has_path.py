from typing import Dict, List, AnyStr, Union

graph_input = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def has_path_dfs(
        graph: Dict[str, Union[List[AnyStr], List]],
        src, dst: str
) -> bool:
    if src == dst:
        return True

    stack = [src]

    while len(stack) > 0:
        curr = stack.pop()
        if curr == dst:
            return True

        for i in graph[curr]:
            stack.append(i)

    return False


def has_path_dfs_recursive(
        graph: Dict[str, Union[List[AnyStr], List]],
        src, dst: str
) -> bool:
    if src == dst:
        return True

    for i in graph[src]:
        if has_path_dfs_recursive(graph, i, dst):
            return True

    return False


def has_path_bfs(
        graph: Dict[str, Union[List[AnyStr], List]],
        src, dst: str
) -> bool:
    if src == dst:
        return True

    q = [src]

    while len(q) > 0:
        curr = q.pop()
        if curr == dst:
            return True

        for i in graph[curr]:
            q.insert(0, i)

    return False


if __name__ == '__main__':
    # print(has_path_dfs_recursive(graph_input, "a", "f"))
    print(has_path_bfs(graph_input, "e", "f"))
