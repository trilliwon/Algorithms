class Solution {
    func maxIncreaseKeepingSkyline(_ grid: [[Int]]) -> Int {
        var rowMax = [Int]()
        var colMax = [Int]()
        
        // row max
        for row in grid {
            rowMax.append(row.max()!)
        }
        
        // col max
        for colIndex in 0..<grid[0].count {
            var cm = 0
            for rowIndex in 0..<grid.count {
                cm = max(cm, grid[rowIndex][colIndex])
            }
            colMax.append(cm)
        }

        var answer = 0
        for row in 0..<grid.count {
            for col in 0..<grid[0].count {
                answer += (min(rowMax[row], colMax[col]) - grid[row][col])
            }
        }
        return answer
    }
}
