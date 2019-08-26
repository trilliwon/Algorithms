class Solution {
    func maxArea(_ height: [Int]) -> Int {
        var ans = 0
        var left = 0
        var right = height.count - 1
        while left < right {
            let lh = height[left]
            let rh = height[right]
            let area = min(lh, rh) * (right - left)
            ans = max(ans, area)
            if lh < rh {
                left += 1
            } else {
                right -= 1
            }
        }
        return ans
    }
}
