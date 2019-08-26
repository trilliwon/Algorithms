class Solution {
    func minAddToMakeValid(_ S: String) -> Int {
        var stack = [String]()
        var S = S.map { String($0) }
        var answer = 0
        
        for c in S {
            if c == "(" {
                stack.append(c)
            } else {
                if let close = stack.popLast() {
                    
                } else {
                    answer += 1
                }
            }
        }

        answer += stack.count
        return answer
    }
}
