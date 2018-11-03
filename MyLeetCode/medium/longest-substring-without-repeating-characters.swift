class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var ans = 0
        var currIndex = 0
        var sArr = Array(s)
        let sLength = s.count
        
        while currIndex < sLength {
            var cacheDic = [Character: Int]()

            for index in currIndex..<sLength {
                if let savedIndex = cacheDic[sArr[index]] {
                    ans = max(ans, index - currIndex)
                    currIndex = savedIndex + 1
                    break
                } else {
                    cacheDic[sArr[index]] = index
                    if index == sLength - 1 {
                        ans = max(ans, sLength - currIndex)
                        currIndex = index + 1
                    }
                }
            }
        }

        return ans
    }
}
