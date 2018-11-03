class Solution {
     func partitionDisjoint(_ A: [Int]) -> Int {
        if A.isEmpty {
            return 0
        }

        var indexAndMin: (Int, Int) = (0, A[0])

        // find min - O(N)
        for (i, v) in A.enumerated() {
            if indexAndMin.1 >= v {
                indexAndMin = (i, v)
            }
        }

        // find left max - O(N)
        var leftMax = 0
        for i in 0...indexAndMin.0 {
            leftMax = max(A[i], leftMax)
        }

        // find right less - O(N)
        var pivotIndex = 0
        var leftMaxCandidate = leftMax
        var i = indexAndMin.0

        while i < A.count {
            leftMaxCandidate = max(A[i], leftMaxCandidate)

            if A[i] < leftMax {
                leftMax = leftMaxCandidate
                pivotIndex = i
            }
            i += 1
        }

        return pivotIndex + 1
    }
}
