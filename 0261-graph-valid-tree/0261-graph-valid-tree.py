class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False


        graph = defaultdict(list)
        for f, s in edges:
            graph[f].append(s)
            graph[s].append(f)

        # visited = [0] * n
        s = set()

        def dfs(x, pre):
            if x in s:
                return False
            s.add(x)
            for i in graph[x]:
                if i != pre:
                    if not dfs(i, x):
                        return False
            return True

        if not dfs(0, -1):
            return False
        if len(s) != n:
            return False
        return True