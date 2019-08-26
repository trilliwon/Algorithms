class Solution {
    func sortArrayByParity(_ A: [Int]) -> [Int] {
        return A.filter { $0 % 2 == 0 } + A.filter { $0 % 2 == 1}
    }
}
