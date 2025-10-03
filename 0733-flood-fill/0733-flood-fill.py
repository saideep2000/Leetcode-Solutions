class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        moves = [[0,1], [1,0], [-1,0], [0,-1]]
        m, n = len(image), len(image[0])

        changeColor = set()



        def search(x, y):
            if (x,y) in changeColor:
                return
            
            changeColor.add((x,y))
            now = image[x][y]
            image[x][y] = color

            for mx, my in moves:
                nx, ny = x + mx, y + my
                if 0 <= nx < m and 0 <= ny < n and image[nx][ny] == now:
                    search(nx, ny)

        
        search(sr, sc)

        return image