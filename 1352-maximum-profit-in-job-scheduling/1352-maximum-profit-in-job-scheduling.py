class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        """
        jobs = [(1,3,50), (2,4,10), ()]
        """
        jobs = []
        memo = {}

        for i in range(len(profit)):
            jobs.append([startTime[i], endTime[i], profit[i]])

        jobs.sort(key=lambda x:x[0])

        def binary_search(i):
            target_time = jobs[i][1]
            left = i + 1
            right = len(jobs) - 1
            result = len(jobs)
            
            while left <= right:
                mid = (left + right) // 2
                if jobs[mid][0] >= target_time:
                    result = mid 
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return result

        def dfs(i):
            if i == len(jobs):
                return 0
            if i in memo:
                return memo[i]

            # don't include
            res = dfs(i+1)

            # include
            # j = i + 1
            # while j < len(jobs):
            #     if jobs[i][1] <= jobs[j][0]:
            #         break
            #     j = j + 1
            j = binary_search(i)


            res = max(res, jobs[i][2] + dfs(j))

            memo[i] = res

            return res
        

        return dfs(0)

        