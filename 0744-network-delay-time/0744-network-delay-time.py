class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        visited = defaultdict(int)

        for i, j, r in times:
            graph[i].append([j,r])

        qu = [(0, k)]

        heapq.heapify(qu)
        
        while qu:
            time, now = heapq.heappop(qu)
            if now in visited:
                continue
            visited[now] = time

            for s,est in graph[now]:
                heapq.heappush(qu, (est+time, s))

        if len(visited) != n:
            return -1

        return max(visited.values())