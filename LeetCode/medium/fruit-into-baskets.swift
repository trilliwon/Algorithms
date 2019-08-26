class Solution {
    func totalFruit(_ tree: [Int]) -> Int {
        
        var answer = 0
        var counter = [Int: Int]()
        var beforeIndex = 0
        var beforeFruit = tree[0]

        for (i, curr) in tree.enumerated() {

            if counter.count == 2 && counter[curr] == nil {
                answer = max(answer, counter.values.reduce(0, +))
                counter = [tree[i-1]: i - beforeIndex]
            }
            
            if curr != beforeFruit {
                beforeIndex = i
                beforeFruit = curr
            }
            counter[curr, default: 0] += 1
        }

        return max(answer, counter.values.reduce(0, +))
    }
}
