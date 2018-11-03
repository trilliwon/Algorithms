class Solution {
    func numberOfLines(_ widths: [Int], _ S: String) -> [Int] {
        var numLine = 1
        var width = 0

        for c in S {
            width = width + widths[Int(c.unicodeScalars.first!.value-97)]
            if width > 100 {
                width = widths[Int(c.unicodeScalars.first!.value-97)]
                numLine += 1
            }
        }
        return [numLine, width]
    }
}
