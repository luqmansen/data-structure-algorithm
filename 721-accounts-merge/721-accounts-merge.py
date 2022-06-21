

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph, name_map = self.build_graph(accounts)
        acc_list = []
        visited = set()
        for node in graph:
            l = self.dfs(node, graph, visited)
            if l is not None:
                acc_list.append([node, *l])

        # remove dup
        for i, v in enumerate(acc_list):
            acc_list[i] = sorted(set(v))

        for e in acc_list:
            name = name_map[e[0]]
            e.insert(0, name)

        return acc_list

    def dfs(self, node, graph, visited=None):
        if node in visited:
            return None

        visited.add(node)

        trace = []
        for neighbor in graph[node]:
            ret = self.dfs(neighbor, graph, visited)
            if ret is not None:
                trace = [*trace, *ret, neighbor]
            else:
                trace = [*trace, neighbor]

        return trace

    def build_graph(self, accounts: List[List[str]]):
        name_map = {}
        graph = {}
        for acc in accounts:
            name = acc[0]
            for e in range(1, len(acc)):
                name_map[acc[e]] = name

            if len(acc) == 2:
                graph[acc[1]] = []
            else:
                # 1 2 3 => {1 :[2], 2:[1], 3:}
                first = acc[1]
                for idx in range(2, len(acc)):
                    e = acc[idx]
                    if first not in graph:
                        graph[first] = []
                    graph[first].append(e)

                    if e not in graph:
                        graph[e] = []
                    graph[e].append(first)

        return graph, name_map
