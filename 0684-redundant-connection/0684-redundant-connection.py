class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(x, pre):
            if x in visited:
                return True
            visited.add(x)
            for j in graph[x]:
                if j != pre:
                    if dfs(j, x):
                        return True
            return False

        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

            visited = set()
            
            if dfs(i,-1):
                return [i,j]
        return [i,j]
