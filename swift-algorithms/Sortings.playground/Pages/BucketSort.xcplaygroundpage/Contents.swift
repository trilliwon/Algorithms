//: [Previous](@previous)


/*:

 # Bucket Sort

 ### Runtime:
 - Best: O(N + K)
 - Average: O(N + K)
 - Worst: O(N^2)

 ### Memory:
 - O(N)

 ```swift

 var items = [6, 2, 7, 4, 5, 10]
 items.bucketSort() // in place sorting
 let sortedItems = items.bucketSorted() // return sorted array

 ```

 */


extension Array where Element == Int {

    public func bucketSorted() -> [Element] {
        guard let max = self.max() else {
            return self
        }

        // build buckets
        var buckets: [[Int]] = (0..<self.count).map ({ _ in [Int]() })

        for item in self {
            // compute bucket index : (value / (maxValue + 1)) * size
            let bucketIndex = (item / (max + 1)) * count
            // insert
            buckets[bucketIndex].append(item)
        }

        var result = [Element]()
        for bucket in buckets {
            result.append(contentsOf: bucket.sorted())
        }

        return result
    }

    public mutating func bucketSort() {
        self = self.bucketSorted()
    }

    var isSorted: Bool {
        if self.isEmpty {
            return true
        }

        for i in 1..<count {
            if self[i - 1] > self[i] {
                return false
            }
        }

        return true
    }
}

var items = (0...20).map ({ _ in Int.random(in: Range(uncheckedBounds:  (0, 100))) })
items.shuffle()
print("Array to be sorted => ", items)

items.bucketSort()
print("Sorted in place    => ", items)
assert(items.isSorted)

print("-----")

items.shuffle()
print("Array to be sorted => ", items)

let sortedItems = items.bucketSorted()
print("Sorted in place    => ", sortedItems)
assert(sortedItems.isSorted)

//: [Next](@next)
