class Solution {
    func sortArrayByParityII(_ A: [Int]) -> [Int] {
        var odd = A.filter{ $0 % 2 == 1 }
        var even = A.filter{ $0 % 2 == 0 }
        var length = A.count
        var A = [Int]()
        for i in 0..<length {
            if i % 2 == 0 {
                A.append(even.removeLast())
            } else {
                A.append(odd.removeLast())
            }
        }
        return A
    }
}
