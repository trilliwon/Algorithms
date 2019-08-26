class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        [2,1,1]
        [1,1,0]
        [0,1,1]
        
        [2,1,1],
        [0,1,1],
        [1,0,1]
        """

        if len(grid) == 0:
            return 0
        
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROTTEN = 2
        FRESH = 1
        EMPTY = 0
        
        temp = []
        box = []
        
        minute = 0
        height = len(grid)
        width = len(grid[0])
    
        # check rotten oranges
        for x in range(height):
            for y in range(width):
                if grid[x][y] == ROTTEN:
                    box.append((x, y))

        while len(box) != 0:
            temp = box
            box = []
            while len(temp) != 0:
                x, y = temp.pop()
                for (dx, dy) in move:
                    mx = x + dx
                    my = y + dy
                    if mx >= 0 and mx < height and my >= 0 and my < width and grid[mx][my] == FRESH:
                        grid[mx][my] = ROTTEN
                        box.append((mx, my))

            if len(box) != 0:
                minute += 1
        
        for x in range(height):
            for y in range(width):
                if grid[x][y] == FRESH:
                    return -1
        return minute
