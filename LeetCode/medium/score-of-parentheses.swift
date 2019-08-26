class Solution {
    func scoreOfParentheses(_ S: String) -> Int {
        if S.count == 0 {
            return 0
        }

        let S = Array(S).map{ String($0) }
        var stack = [String]()

        for paren in S {

            if paren == "(" {
                stack.append(paren)
            } else {

                var sum = 0
                while stack.last! != "(", let n = stack.popLast() {
                    sum += Int(n)!
                }

                if let p = stack.popLast(), p == "(" {

                    if sum != 0 {
                        stack.append("\(sum * 2)")
                    } else {
                        stack.append("1")
                    }
                }
            }
        }

        return stack.reduce(0, { $0 + Int($1)! })
    }
}
