//: [Previous](@previous)


/*:

 # Counting Sort

 ### Runtime:
 - Best: O(N + K)
 - Average: O(N + K)
 - Worst: O(N + K)

 ### Memory:
 - O(K)

 ```swift

 var items = [6, 2, 7, 4, 5, 10]
 items.countingSort() // in place sorting
 let sortedItems = items.countingSorted() // return sorted array

 ```

 */


extension Array where Element == Int {

    public func countingSorted() -> [Element] {
        guard let max = self.max() else {
            return self
        }

        // Initialize counting array to all zeros.
        var countingArray = Array(repeating: 0, count: max + 1)

        // Initialize output array to all zeros.
        var outputArray = Array(repeating: 0, count: count)

        // Count the number of times each value occurs in the input.
        for item in self {
            countingArray[item] += 1
        }

        // Modify the counting array to give the number of values smaller than index
        for i in 1..<countingArray.count {
            countingArray[i] += countingArray[i - 1]
        }

        // Transfer numbers from input to output array at locations provided by counting array
        for item in reversed() {
            countingArray[item] -= 1
            outputArray[countingArray[item]] = item
        }

        return outputArray
    }

    public mutating func countingSort() {
        self = self.countingSorted()
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

var items = (0...20).map ({ _ in Int.random(in: Range(uncheckedBounds:  (0, 7))) })
items.shuffle()
print("Array to be sorted => ", items)

items.countingSort()
print("Sorted in place    => ", items)
assert(items.isSorted)

print("-----")

items.shuffle()
print("Array to be sorted => ", items)

let sortedItems = items.countingSorted()
print("Sorted in place    => ", sortedItems)
assert(sortedItems.isSorted)

//: [Next](@next)
