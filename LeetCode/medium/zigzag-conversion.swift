class Solution {
    func convert(_ s: String, _ numRows: Int) -> String {
        if s == "" || numRows == 1 {
            return s
        }

        let count = s.count
        var s = Array(s)
        var container = Array(repeating: [Character](), count: numRows)
        let boundary: Int = (count / ((numRows * 2) - 2)) + 1
        var index = 0

        for _ in 0..<boundary {
            for j in 0..<numRows {
                guard index < count else {
                    break
                }
                container[j].append(s[index])
                index += 1
            }

            for j in (1..<(numRows-1)).reversed() {
                guard index < count else {
                    break
                }
                container[j].append(s[index])
                index += 1
            }
        }

        return container.compactMap({ $0 }).reduce("", +)
}
}
