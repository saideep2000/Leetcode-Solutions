class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        finalCost = [float(+inf)]* n
        finalCost[src] = 0
        for i in range(0,k+1):
            temp = finalCost.copy()
            for start, stop, cost in flights:
                if finalCost[start] != float(+inf):
                    temp[stop] = min(temp[stop], finalCost[start] + cost)
            finalCost = temp.copy()
        if finalCost[dst] == float(+inf):
            return -1
        return finalCost[dst]


        # visited = set()
        # minH = [[0,src]]
        # graph = defaultdict(list)
        # rem = 0
        # for i, j, dist in flights:
        #     graph[i].append([j, dist])
        # while minH:
        #     flag = 1
        #     if k == -1:
        #         while flag and minH:
        #             node_dist, node = heapq.heappop(minH)
        #             if node == dst:
        #                 flag = 0
        #     else:
        #         node_dist, node = heapq.heappop(minH)
        #     print(rem, node)
        #     if node == dst:
        #         return rem
            
        #     if node in visited:
        #         continue
        #     visited.add(node)
            
        #     k = k - 1
        #     if len(graph[node]) == 0:
        #         return -1
        #     for i, i_dist in graph[node]:
        #         if i not in visited:
        #             m = node_dist + i_dist
        #             heapq.heappush(minH, [m, i])
        #             rem = m
        # return rem