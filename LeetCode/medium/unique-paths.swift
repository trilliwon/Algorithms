class Solution {
    func uniquePaths(_ m: Int, _ n: Int) -> Int {
        var x = 0
        var y = 0
        var cache = Array(repeating: Array(repeating: 1, count: m), count: n)
                
        for i in 1..<n {
            for j in 1..<m {
                cache[i][j] = cache[i-1][j] + cache[i][j-1]
            }
        }
        
        return cache[n-1][m-1]
    }
}
