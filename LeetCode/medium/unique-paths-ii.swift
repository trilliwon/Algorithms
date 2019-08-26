class Solution {
    func uniquePathsWithObstacles(_ obstacleGrid: [[Int]]) -> Int {
        
        if obstacleGrid[0][0] == 1 {
            return 0
        }
        
        var obstacleGrid = obstacleGrid
        var n = obstacleGrid.count
        var m = obstacleGrid[0].count

        (0..<n).forEach { obstacleGrid[$0][0] = obstacleGrid[$0][0] == 1 ? 0 : 1 }
        (0..<m).forEach { obstacleGrid[0][$0] = obstacleGrid[0][$0] == 1 ? 0 : 1 }
        
        obstacleGrid[0][0] = 1

        (1..<n).forEach { obstacleGrid[$0][0] = obstacleGrid[$0][0] == 0 ? 0 : obstacleGrid[$0-1][0] }
        (1..<m).forEach { obstacleGrid[0][$0] = obstacleGrid[0][$0] == 0 ? 0 : obstacleGrid[0][$0-1] }
 
        (1..<n).forEach { i in
            (1..<m).forEach { j in
                if obstacleGrid[i][j] == 1 {
                    obstacleGrid[i][j] = 0
                } else {
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                }
            }
        }

        return obstacleGrid[n-1][m-1]
    }
}
