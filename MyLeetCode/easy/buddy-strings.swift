class Solution {
    func buddyStrings(_ A: String, _ B: String) -> Bool {
        if A.count != B.count {
            return false
        }
        
        var dictA = [Character: Int]()
        for c in A {
            dictA[c, default: 0] += 1
        }
        
        var dictB = [Character: Int]()
        for c in B {
            dictB[c, default: 0] += 1
        }
                
        if A == B {
            return dictA.count != A.count
        }
        
        if dictA == dictB {
            var arrA = Array(A)
            var diff = 0
            for (i, c) in B.enumerated() {
                if c != arrA[i] {
                    diff += 1
                }
            }
            if diff == 2 {
                return true
            }
        }
        
        return false
    }
}
