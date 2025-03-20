class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        rule = defaultdict(list)
        for course, pre in prerequisites:
            rule[course].append(pre)

        visited = [0]*numCourses
        final = []

        def dfs(course) -> bool:
            if visited[course] == 1:
                return False
            visited[course] = 1
            for each in rule[course]:
                if not dfs(each):
                    return False
            if course not in final:
                final.append(course)
            visited[course] = 2
            return True
        
        for i in range(0,numCourses):
            if not dfs(i):
                return []
        return final