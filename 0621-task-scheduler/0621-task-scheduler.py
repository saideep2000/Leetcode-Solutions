class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time = time + 1
            if maxHeap:
                now = 1 + heapq.heappop(maxHeap)
                if now:
                    q.append([now, time+n])
            if q and q[0][1] == time:
                q_now = q.popleft()
                if q_now[0] != 0:
                    heapq.heappush(maxHeap, q_now[0])
                
        return time