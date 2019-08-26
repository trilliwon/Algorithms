class Solution {
   func rowAndCol(s: Int, N: Int) -> (Int, Int) {
        var s = s - 1
        var row = N - (s / N) - 1
        var col = row % 2 != N % 2 ? s % N : N - 1 - (s % N)
        return (row, col)
    }

    func snakesAndLadders(_ board: [[Int]]) -> Int {

        var N = board.count
        var cache = [1: 0]
        var queue = [Int]()
        queue.append(1)

        while !queue.isEmpty {

            var curr = queue.removeFirst() // pop
            
            if curr == N*N {
                return cache[curr]!
            }

            for var next in curr+1...min(curr+6, N*N) {
                let rc = rowAndCol(s: next, N: N)

                if board[rc.0][rc.1] != -1 {
                    next = board[rc.0][rc.1]
                }

                if cache[next] == nil {
                    cache[next] = cache[curr]! + 1
                    queue.append(next)
                }
            }
        }
        return -1
    }
}
