class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        rem = [[0] * numCourses for _ in range(numCourses)]

        for dx, dy in prerequisites:
            rem[dx][dy] = 1
        
        visited = [0] * numCourses

        def dfs(x,vi):
            if vi[x] == 1:
                return False
            if vi[x] == 2:
                return True
            vi[x] = 1
            for k in range(0,numCourses):
                if rem[x][k] == 1:
                    if not dfs(k,vi):
                        return False
            vi[x] = 2
            return True

        for i in range(0,numCourses):
            if not dfs(i,visited):
                return False
        return True
                