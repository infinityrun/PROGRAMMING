class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def search_neighbour(grid, i, j) -> int:
            if 0 <= i < len(grid) and 0<= j < len(grid[i]) and grid[i][j] == "1":
                grid[i][j] = "0"
                for di,dj in directions:
                    p,q = i+di, j+dj
                    search_neighbour(grid, p, q)
                return 1
            return 0
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = collections.deque([])
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result += search_neighbour(grid, i,j)
        return result

#Answer 2
def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)) # Map function works horizontally, where as the zip function work vertically.
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
