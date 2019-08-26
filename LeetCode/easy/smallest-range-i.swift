class Solution {
    func smallestRangeI(_ A: [Int], _ K: Int) -> Int {
        if A.isEmpty {
            return 0
        }
        
        let diff = A.max()! - A.min()! - (K*2)
        if diff < 0 {
            return 0
        } else {
            return diff
        }
    }
}
