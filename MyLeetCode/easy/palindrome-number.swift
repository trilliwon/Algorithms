class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        guard let reversed: Int = Int(String(x).characters.map { "\($0)" }.reversed().reduce("") { $0 + $1 }) else { return false }
        return reversed == x
    }
}
