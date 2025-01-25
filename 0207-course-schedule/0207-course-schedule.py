class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Build adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        vi = [0] * numCourses

        def dfs(x):
            if vi[x] == 1:
                return False
            if vi[x] == 2:
                return True
            vi[x] = 1
            for k in graph[x]:
                if not dfs(k):
                    return False
            vi[x] = 2
            return True

        for i in range(0,numCourses):
            if not dfs(i):
                return False
        return True
                