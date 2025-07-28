class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)

        for idx, each in enumerate(manager):
            if each != -1:
                adj[each].append(idx)
        
        q = deque([(headID, 0)])
        storeMax = 0

        while q:
            node, time = q.popleft()

            storeMax = max(storeMax, time)

            for each in adj[node]:
                q.append((each, time + informTime[node]))
        
        return storeMax
