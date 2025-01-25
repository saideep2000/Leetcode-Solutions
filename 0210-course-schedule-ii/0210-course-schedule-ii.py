class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        final = []

        visited = [0] * numCourses

        def dfs(x):
            if visited[x] == 1:
                return False
            visited[x] = 1
            for n in graph[x]:
                if not dfs(n):
                    return False
            if x not in final:
                final.append(x)
            visited[x] = 2
            return True

        for i in range(0,numCourses):
            if not dfs(i):
                return []

        return final