class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime = sorted(processorTime) #nlogn
        tasks = sorted(tasks, reverse = True) #nlogn
        curr = 0
        final_time = 0
        print(processorTime, tasks)
        for i in range(0,len(processorTime)): #O(n)
            final_time = max(final_time, processorTime[i]+tasks[curr]) #O(1)
            curr = curr + 4
        return final_time