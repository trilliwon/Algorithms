class Solution {
    func minPathSum(_ grid: [[Int]]) -> Int {
        var grid = grid
        let n = grid.count
        let m = grid[0].count
        
        (1..<n).forEach {  grid[$0][0] += grid[$0-1][0] }
        (1..<m).forEach { grid[0][$0] += grid[0][$0-1] }
        
        for i in 1..<n {
            for j in 1..<m {
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
            }
        }
        
        return grid[n-1][m-1]
    }
}
