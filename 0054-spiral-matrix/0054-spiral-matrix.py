class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Conditions : 
        1. Uneven / Unsymmetric matrix : Yes
        2. Will there be any empty matrix given : Yes
        3. Empty fields given : No
        4. Can it have empty matrix altogether : No

        Thought: 
        4 directions:
        1.Right
        2.Down
        3.Left
        4.Up

        123
        456
        789

        """

        moves = [[0,1], [1,0], [0,-1], [-1,0]]
        m, n = len(matrix), len(matrix[0])
        store = set()
        total = m*n

        # intitialize the final list
        final_list = []

        # simple dfs to deep dive in given condition
        def dfs(x, y, dir_index):
            # stopping point
            if len(final_list) == total:
                return
            # visited
            store.add((x,y))
            final_list.append(matrix[x][y])
            # looping point
            for i in range(4):
                new_dir = (dir_index+i)%4
                mx = moves[new_dir][0]
                my = moves[new_dir][1]
                if x+mx >= 0 and x+mx < m and y+my >= 0 and y+my < n and (x+mx,y+my) not in store:
                    dfs(x+mx, y+my, new_dir)
                    break

        # calling the dfs
        dfs(0,0,0)

        # returning
        return final_list
