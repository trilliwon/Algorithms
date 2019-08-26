class Solution {
    func isAlpha(char: Character) -> Bool {
        switch char {
        case "a"..."z":
            return true
        case "A"..."Z":
            return true
        default:
            return false
        }
    }
    
    func reverseOnlyLetters(_ S: String) -> String {
        var S = S.map({ $0 })
        var i = 0
        var j = S.count - 1
        
        while i < j {
            if isAlpha(char: S[i]) && isAlpha(char: S[j]) {
                S.swapAt(i, j)
                i += 1
                j -= 1
            } else {
                if !isAlpha(char: S[i]) {
                    i += 1
                }
                
                if !isAlpha(char: S[j]) {
                    j -= 1
                }
            }
        }
        
        return S.reduce("", { $0 + String($1) })
    }
}
