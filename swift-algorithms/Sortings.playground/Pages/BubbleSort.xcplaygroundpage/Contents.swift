//: [Previous](@previous)

/*:

 # Bubble Sort

 ### Runtime:
 - Best: O(N)
 - Average: O(N^2)
 - Worst: O(N^2)

 ### Memory:
 - O(1)

 ```swift

 var items = [6, 2, 7, 4, 5, 10]
 items.bubbleSort() // in place sorting
 let sortedItems = items.bubbleSorted() // return sorted array

 ```

 */

extension Array where Element : Comparable {

    public mutating func bubbleSort() {
        for i in 0..<count {
            for j in 1..<(count - i) {
                if self[j - 1] > self[j] {
                    self.swapAt(j, j - 1)
                }
            }
        }
    }

    public func bubbleSorted() -> [Element] {
        var elements = self
        elements.bubbleSort()
        return elements.sorted()
    }
}

var items = [6, 2, 7, 4, 5, 10]
items.shuffle()
print("Array to be sorted => ", items)

items.bubbleSort()
print("Sorted in place    => ", items)

print("----")

items.shuffle()
print("Array to be sorted => ", items)

let sortedItems = items.bubbleSorted()
print("Sorted in place    => ", sortedItems)


//: [Next](@next)
