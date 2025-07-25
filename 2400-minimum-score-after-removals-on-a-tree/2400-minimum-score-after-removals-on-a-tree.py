from collections import defaultdict
from typing import List

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(nums)
        tin = [0] * n
        tout = [0] * n
        xor = [0] * n
        parent = [-1] * n
        time = 0

        # Build tree
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # DFS to get subtree XORs and in/out times
        def dfs(u, p):
            nonlocal time
            tin[u] = time
            time += 1
            xor[u] = nums[u]
            parent[u] = p
            for v in adj[u]:
                if v != p:
                    dfs(v, u)
                    xor[u] ^= xor[v]
            tout[u] = time
            time += 1

        dfs(0, -1)
        total_xor = xor[0]

        def is_ancestor(u, v):
            return tin[u] <= tin[v] and tout[v] <= tout[u]

        res = float('inf')
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                # Always treat the child as the one not being the parent
                u1, v1 = edges[i]
                c1 = v1 if parent[v1] == u1 else u1
                u2, v2 = edges[j]
                c2 = v2 if parent[v2] == u2 else u2

                if is_ancestor(c1, c2):
                    x = xor[c2]
                    y = xor[c1] ^ xor[c2]
                    z = total_xor ^ xor[c1]
                elif is_ancestor(c2, c1):
                    x = xor[c1]
                    y = xor[c2] ^ xor[c1]
                    z = total_xor ^ xor[c2]
                else:
                    x = xor[c1]
                    y = xor[c2]
                    z = total_xor ^ xor[c1] ^ xor[c2]

                res = min(res, max(x, y, z) - min(x, y, z))

        return res
