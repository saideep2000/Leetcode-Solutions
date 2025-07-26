class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # initialise
        rev_graph = defaultdict(list)
        n = len(graph)
        inDegree = [0]*n
        q = deque()

        # Step 1 : Reverse the curr graph
        for u in range(n):
            for v in graph[u]:
                rev_graph[v].append(u)
                inDegree[u] = inDegree[u] + 1
        
        # Step 2 : Find the in-degree of the zero which are the terminal nodes
        for idx, each in enumerate(inDegree):
            if each == 0:
                q.append(idx)
        
        result = []

        # Step 3 : 
        while q:
            node = q.popleft()
            result.append(node)

            for each in rev_graph[node]:
                inDegree[each] -= 1
                if inDegree[each] == 0:
                    q.append(each)
        

        return sorted(result)
        

                