class Solution {
    func hasGroupsSizeX(_ deck: [Int]) -> Bool {
        if deck.isEmpty {
            return false
        }
        let counter = deck.reduce(into: [:]) { counts, elem in counts[elem, default: 0] += 1 }
        let values = counter.values

        let maxCount = values.max()!

        if values.min()! < 2 {
            return false
        }

        for div in 2...maxCount {
            if (values.reduce(true) { $0 && ($1 % div == 0) }) {
                return true
            }
        }

        return false
    }
}
