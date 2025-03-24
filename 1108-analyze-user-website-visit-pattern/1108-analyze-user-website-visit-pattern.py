from collections import defaultdict
from typing import List

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Step 1: Combine logs and sort by timestamp.
        logs = sorted(zip(timestamp, username, website))
        
        # Step 2: Group website visits by user.
        user_visits = defaultdict(list)
        for t, user, site in logs:
            user_visits[user].append(site)
        
        # Global dictionary to count each unique 3-sequence pattern.
        pattern_count = defaultdict(int)
        
        # DFS helper to generate all unique 3-sequence patterns from visits.
        def generate_patterns(visit, start, path, result):
            if len(path) == 3:
                result.add(tuple(path))
                return
            for i in range(start, len(visit)):
                path.append(visit[i])
                generate_patterns(visit, i + 1, path, result)
                path.pop()
        
        # Process each user's visits.
        for user, visits in user_visits.items():
            if len(visits) < 3:
                continue
            user_patterns = set()
            generate_patterns(visits, 0, [], user_patterns)
            # Increase count for each unique pattern for the user.
            for pattern in user_patterns:
                pattern_count[pattern] += 1
        
        # Step 3: Find the pattern with the highest count.
        max_count = 0
        result_pattern = tuple()
        for pattern, count in pattern_count.items():
            # Tie-break: lexicographically smallest pattern if counts are equal.
            if count > max_count or (count == max_count and (not result_pattern or pattern < result_pattern)):
                max_count = count
                result_pattern = pattern
        
        return list(result_pattern)
