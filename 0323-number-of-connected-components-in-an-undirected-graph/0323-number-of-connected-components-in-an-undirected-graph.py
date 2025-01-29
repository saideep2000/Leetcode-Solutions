class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        visited = set()
        numb = 0

        def dfs(x, pre):
            if x in visited:
                return
            visited.add(x)
            for i in graph[x]:
                if pre != i:
                    dfs(i, x)
            return
        
        for i in range(0,n):
            if i not in visited:
                dfs(i, -1)
                numb = numb + 1
        return numb